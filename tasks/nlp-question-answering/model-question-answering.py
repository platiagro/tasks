import torch
import numpy as np
from nlgeval import NLGEval
from multiprocessing import cpu_count
from transformers import AutoModelForQuestionAnswering
from torch.utils.data import DataLoader
import pytorch_lightning as pl


class Metrics_Calculator(object):

    def __init__(self,tokenizer,nlg_eval):
        #super(Metrics_Calculator, self).__init__()
        self.nlg_eval = nlg_eval
        self.list_dict_track  = {"data":[]}
        self.tokenizer = tokenizer
        #self.glove_comparer = glove_comparer
        self.softmax = torch.nn.Softmax(dim=0)

        
    def build_json_results(self,
                           question,
                           context,
                           expected_answer,
                           generated_answer,
                           metrics_dict):

        """
        Cria json para cada linha que será salvo para monitorar as métricas em self.list_dict_track
        """
        new_info = {}
        new_info["question"] =question
        new_info["context"] =context
        new_info["expected_answer"] =expected_answer
        new_info["generated_answer"] =generated_answer
        new_info["metrics_dict"] =metrics_dict
        return new_info

    
    def compute_metrics(self,input_ids_batch,pred_start_logits_batch,pred_end_logits_batch,start_positions_batch,end_positions_batch,save_track_dict=False):
        """
        Calcula métricas para todo o batch
        """
        batch_bleu_1_list = []
        batch_bleu_2_list = []
        batch_bleu_3_list = []
        batch_bleu_4_list = []
        batch_CIDEr_list = []
        batch_ROUGE_L_list = []
        #batch_Glove_Cossine_Similarity_list = []

        #batch
        for i in range(len(input_ids_batch)):
            input_ids = input_ids_batch[i]
            text = self.tokenizer.decode(input_ids)
            text_parts = text.split(self.tokenizer.sep_token)
            question = text_parts[0].split(self.tokenizer.cls_token)[1].strip()
            context = text_parts[1].strip()

            pred_start_logit = pred_start_logits_batch[i]
            pred_end_logit = pred_end_logits_batch[i]
            pred_start_position = self.softmax(pred_start_logit).argmax().item()
            pred_end_position = self.softmax(pred_end_logit).argmax().item()
            start_position = start_positions_batch[i].item()
            end_position = end_positions_batch[i].item()
            expected_answer = self.tokenizer.decode(input_ids[start_position:end_position+1])
            generated_answer = self.tokenizer.decode(input_ids[pred_start_position:pred_end_position+1])
    

            metrics_dict = self.nlg_eval.compute_individual_metrics(ref=[expected_answer],hyp=generated_answer)#ref:List[str] , hyp:str
            #metrics_dict['cossine_similarity'] = self.glove_comparer.compare_sentences_with_cossine_similarity(original_target,gen_target_option)

            #linha
            #elevant_logits = logits[i*self.hparams.num_gen_sentences:self.hparams.num_gen_sentences+i*self.hparams.num_gen_sentences]
            #gen_target_options_list = [self.hparams.tokenizer.decode(l, skip_special_tokens=True) for l in relevant_logits]

            if save_track_dict:
                self.list_dict_track["data"].append(self.build_json_results(question= question,
                                                                          context= context,
                                                                          expected_answer=expected_answer,
                                                                          generated_answer=generated_answer,
                                                                          metrics_dict = metrics_dict))
                
            
            batch_bleu_1_list.append(metrics_dict['Bleu_1'])
            batch_bleu_2_list.append(metrics_dict['Bleu_2'])
            batch_bleu_3_list.append(metrics_dict['Bleu_3'])
            batch_bleu_4_list.append(metrics_dict['Bleu_4'])
            batch_CIDEr_list.append(metrics_dict['CIDEr'])
            batch_ROUGE_L_list.append(metrics_dict['ROUGE_L'])
            #batch_Glove_Cossine_Similarity_list.append(metrics_dict['Glove_Cossine_Similarity'])


        batch_metrics_dict = {"Batch_Bleu_1":np.mean(batch_bleu_1_list),
                              "Batch_Bleu_2":np.mean(batch_bleu_2_list),
                              "Batch_Bleu_3":np.mean(batch_bleu_3_list),
                              "Batch_Bleu_4":np.mean(batch_bleu_4_list),
                              "Batch_CIDEr":np.mean(batch_CIDEr_list),
                              "Batch_ROUGE_L":np.mean(batch_ROUGE_L_list),
                              #"Batch_Glove_Cossine_Similarity":np.mean(batch_Glove_Cossine_Similarity_list)
                             }

        return batch_metrics_dict

# https://huggingface.co/transformers/model_doc/bert.html#bertforquestionanswering
class Reader(pl.LightningModule):

    def __init__(self,hparams):
        super(Reader, self).__init__()

        self.hparams = hparams
        pl.utilities.seed.seed_everything(seed = self.hparams.seed)

        # ---------- Model
        self.model = AutoModelForQuestionAnswering.from_pretrained(self.hparams.model_name)

        
        #----------Metrics Trackers
        if self.hparams.stage == 'Experiment':

            #glove_comparer = Glove_Embeddings_Comparer(glove_weights_path=self.hparams.glove_weights_path,device=self.hparams.device)
            self.nlg_eval = NLGEval(metrics_to_omit=['EmbeddingAverageCosineSimilairty', 'EmbeddingAverageCosineSimilarity','GreedyMatchingScore','SkipThoughtCS','VectorExtremaCosineSimilarity'])
            self.valid_metrics_calculator = Metrics_Calculator(self.hparams.tokenizer,self.nlg_eval)
            self.test_metrics_calculator = Metrics_Calculator(self.hparams.tokenizer,self.nlg_eval)

    def predict(self):
        self.hparams.stage = 'Deployment'

    def forward(self,token_ids,attention_mask,token_type_ids,start_positions=None,end_positions=None):
        if self.hparams.testing  == False:
            output = self.model(input_ids=token_ids, attention_mask=attention_mask, token_type_ids=token_type_ids,start_positions=start_positions, end_positions=end_positions)
        else:
            output = self.model(input_ids=token_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        return output

    def training_step(self, batch, batch_idx):
        self.hparams.testing  = False
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids,start_positions,end_positions)
        loss = output['loss']
        #pred_start_logits = output['start_logits']
        #pred_end_logits = output['end_logits']
        batch_metrics_dict = {'loss':loss}

        return batch_metrics_dict

    def validation_step(self, batch, batch_idx):
        self.hparams.testing  = False
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids,start_positions, end_positions)
        loss = output['loss']
        pred_start_logits = output['start_logits']
        pred_end_logits = output['end_logits']

        #Calc Metrics and Saving Results
        batch_metrics_dict= self.valid_metrics_calculator.compute_metrics(token_ids,pred_start_logits,pred_end_logits,start_positions,end_positions,save_track_dict=True)
        batch_metrics_dict= {'valid_'+key: value for (key, value) in batch_metrics_dict.items()}
        batch_metrics_dict['valid_loss'] = loss.item() 

        #include special values to batch metrics dict
        batch_metrics_dict['loss']  = loss

        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict
  

    def test_step(self, batch, batch_idx):
        self.hparams.testing  = True
        token_ids, attention_mask, token_type_ids, start_positions, end_positions = batch
        output = self.forward(token_ids,attention_mask,token_type_ids)
        pred_start_logits = output['start_logits']
        pred_end_logits = output['end_logits']

        #Calc Metrics and Saving Results
        batch_metrics_dict= self.test_metrics_calculator.compute_metrics(token_ids,pred_start_logits,pred_end_logits,start_positions,end_positions,save_track_dict=True)
        batch_metrics_dict = {'test_'+key: value for (key, value) in batch_metrics_dict.items()}

        for key, value in batch_metrics_dict.items():
            self.log(key, value, on_step=True, prog_bar=True, logger=True)

        return batch_metrics_dict
    
    def training_epoch_end(self, outputs):
        if not outputs:
            return {}
        epoch_dict = self.get_epoch_results(outputs,'train')

    def validation_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'valid')
        return epoch_dict #must do to save checkpoints

    def test_epoch_end(self, outputs):
        epoch_dict = self.get_epoch_results(outputs,'test')


    def get_epoch_results(self,outputs,step='train'):

        tensorboard_logs = {}

        if step != "test":
            temp_avg_loss_batch = [x["loss"] for x in outputs]
            avg_loss = torch.stack(temp_avg_loss_batch).mean()

        if step != "train":
            temp_avg_bleu1_batch = [x[f"{step}_Batch_Bleu_1"] for x in outputs]
            temp_avg_bleu2_batch = [x[f"{step}_Batch_Bleu_2"] for x in outputs]
            temp_avg_bleu3_batch = [x[f"{step}_Batch_Bleu_3"] for x in outputs]
            temp_avg_bleu4_batch = [x[f"{step}_Batch_Bleu_4"] for x in outputs]
            temp_avg_cider_batch = [x[f"{step}_Batch_CIDEr"] for x in outputs]
            temp_avg_rougeL_batch = [x[f"{step}_Batch_ROUGE_L"] for x in outputs] 
            # temp_avg_glove_cossine_similarity = [x["{step}_Batch_Glove_Cossine_Similarity"] for x in outputs] 

            avg_bleu1 = np.stack(temp_avg_bleu1_batch).mean()
            avg_bleu2 = np.stack(temp_avg_bleu2_batch).mean()
            avg_bleu3 = np.stack(temp_avg_bleu3_batch).mean()
            avg_bleu4 = np.stack(temp_avg_bleu4_batch).mean()
            avg_cider = np.stack(temp_avg_cider_batch).mean()
            avg_rougeL = np.stack(temp_avg_rougeL_batch).mean()
            # avg_glove_cossine_similarity = np.stack(temp_avg_glove_cossine_similarity).mean()

            tensorboard_logs[f"avg_{step}_bleu1"] = avg_bleu1
            tensorboard_logs[f"avg_{step}_bleu2"] = avg_bleu2
            tensorboard_logs[f"avg_{step}_bleu3"] = avg_bleu3
            tensorboard_logs[f"avg_{step}_bleu4"] = avg_bleu4
            tensorboard_logs[f"avg_{step}_cider"] = avg_cider
            tensorboard_logs[f"avg_{step}_rougeL"] = avg_rougeL
            #tensorboard_logs[f"avg_{step}_Cossine_Similarity"] = avg_glove_cossine_similarity

        if step != "test":
            tensorboard_logs[f"avg_{step}_loss"] =  avg_loss.item()
            
        for key, value in tensorboard_logs.items():
            self.log(key, value, on_epoch=True, prog_bar=True, logger=True)

        return tensorboard_logs

    def configure_optimizers(self):
        return torch.optim.AdamW(
            [p for p in self.parameters() if p.requires_grad],
            lr=self.hparams.learning_rate, eps=self.hparams.eps)

    def train_dataloader(self):
        self.train_dataset = self.hparams.CustomDataset(
                    df = self.hparams.all_data['train'],
                    tokenizer = self.hparams.tokenizer,
                    max_length = self.hparams.max_length,
                    stage=self.hparams.stage)
        
        # shuffle = False if self.hparams.overfit else True
        return DataLoader(self.train_dataset, batch_size=self.hparams.train_batch_size, shuffle=True,num_workers=cpu_count())
    

    def val_dataloader(self):
        self.valid_dataset = self.hparams.CustomDataset(
                    df = self.hparams.all_data['valid'],
                    tokenizer = self.hparams.tokenizer,
                    max_length = self.hparams.max_length,
                    stage=self.hparams.stage)
        
        return DataLoader(self.valid_dataset, batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())

    def test_dataloader(self):
        self.test_dataset = self.hparams.CustomDataset(
                    df = self.hparams.all_data['test'],
                    tokenizer = self.hparams.tokenizer,
                    max_length = self.hparams.max_length,
                    stage=self.hparams.stage)
        
        return DataLoader(self.test_dataset, batch_size=self.hparams.eval_batch_size, shuffle=False,num_workers=cpu_count())
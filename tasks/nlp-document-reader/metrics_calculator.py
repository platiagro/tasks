import torch
import numpy as np

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
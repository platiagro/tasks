import functools
import traceback
from multiprocessing import cpu_count

import pandas as pd
import psutil
import pytorch_lightning as pl
import torch
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader
from torch.utils.data.sampler import WeightedRandomSampler


class GloveFinetuner(pl.LightningModule):
    def __init__(self, hyperparams, model_parameters, dataset_infos, extra_infos):

        super(GloveFinetuner, self).__init__()

        # ---------- hyperparams
        self.learning_rate = hyperparams["learning_rate"]
        self.train_batch_size = hyperparams["train_batch_size"]
        self.eval_batch_size = hyperparams["eval_batch_size"]
        self.hidden_dim = hyperparams["hidden_dim"]

        # ---------- model_parameters
        self.loss_funtion = model_parameters["criterion"]
        self.label_encoder = model_parameters["label_encoder"]
        self.glove_infos = model_parameters["glove_infos"]

        # ---------- dataset_infos
        self.all_data = dataset_infos["all_data"]
        self.CustomDataset = dataset_infos["CustomDataset"]

        # ---------- extra_infos
        self.overfit = extra_infos["overfit"]
        self.sampler = extra_infos["sampler"]
        self.device = extra_infos["device"]

        # ---------- other_infos
        self.predict_proba = torch.nn.Softmax(dim=1)
        self.step = "Experiment"

        # ---------- Dados para gráfico de Acurácia e Loss
        self.df_performance_train_batch = pd.DataFrame(
            columns=["train_batch_loss", "train_batch_acc"]
        )
        self.df_performance_train_epoch = pd.DataFrame(
            columns=["train_epoch_loss", "train_epoch_acc"]
        )
        self.df_performance_valid_batch = pd.DataFrame(
            columns=["valid_batch_loss", "valid_batch_acc"]
        )
        self.df_performance_valid_epoch = pd.DataFrame(
            columns=["valid_epoch_loss", "valid_epoch_acc"]
        )

        # ---------- Carregamento datasets
        self.targets_sampler = self.all_data[2]
        if self.overfit:
            self.train_dataset = self.CustomDataset(
                self.all_data[0], self.all_data[1], self.all_data[2]
            )
            self.valid_dataset = self.CustomDataset(
                self.all_data[0], self.all_data[1], self.all_data[2]
            )
            self.test_dataset = self.CustomDataset(
                self.all_data[0], self.all_data[1], self.all_data[2]
            )
        else:
            self.train_dataset = self.CustomDataset(
                self.all_data[0], self.all_data[1], self.all_data[2]
            )
            self.valid_dataset = self.CustomDataset(
                self.all_data[3], self.all_data[4], self.all_data[5]
            )
            self.test_dataset = self.CustomDataset(
                self.all_data[6], self.all_data[7], self.all_data[8]
            )
            

        # ---------- Datafame de comparação para o teste
        columns = [ "ORIGINAL_TARGET","ORIGINAL_CODE","PREDICTED_TARGET","PREDICTED_CODE" ] + [label.upper() + "_PROB" for label in self.label_encoder.classes_]
        self.df_valid = pd.DataFrame(columns=columns)
        self.df_test = pd.DataFrame(columns=columns)

        # ---------- Englobamentoda rede para classificação(se necessário)
        weight = self.glove_infos["glove_vectors"]
        embedding_dim = self.glove_infos["glove_dim"]
        output_classes_number = len(self.label_encoder.classes_)
        self.embedding_bag = torch.nn.EmbeddingBag.from_pretrained(
            weight, mode="mean", freeze=True
        )
        self.layer1 = torch.nn.Linear(embedding_dim, self.hidden_dim)
        self.layer2 = torch.nn.Linear(
            self.hidden_dim, output_classes_number
        )

        layers = [self.layer1, self.layer2]

        self.net = torch.nn.Sequential(*layers)

    def predict(self, X_inference_glove_ids, X_inference_glove_words):
        self.step = "Deployment"
        inference_dataset = self.CustomDataset(
            X_inference_glove_ids, X_inference_glove_words,step=self.step
        )
        dataloader = DataLoader(
            inference_dataset,
            batch_size=self.eval_batch_size,
            shuffle=False,
            num_workers=cpu_count(),
            collate_fn=self.my_collate,
        )
        for batch in dataloader:
            batch = [elem.to(self.device) for elem in batch] 
            self.test_step(batch, None)
        return self.df_test

    def forward(self, word_ids, offsets):
        X_emb = self.embedding_bag(word_ids, offsets)
        hidden = torch.relu(self.layer1(X_emb))
        logits = self.layer2(hidden)
        return logits

    def training_step(self, batch, batch_nb):
        # batch
        inputs, offsets, targets = batch
                
        # fwd
        y_hat = self.forward(inputs, offsets)

        # loss
        loss = self.loss_funtion(y_hat, targets)

        # acc
        acc = self.get_acc(y_hat, targets)

        # What to log
        tensorboard_logs = {"loss": loss, "acc": acc}

        self.df_performance_train_batch = self.df_performance_train_batch.append(
            pd.Series(
                [loss.item(), acc.item()], index=self.df_performance_train_batch.columns
            ),
            ignore_index=True,
        )

        return {
            "loss": loss,
            "train_acc_batch": acc,
            "train_loss_batch": loss,
            "log": tensorboard_logs,
        }

    def training_epoch_end(self, outputs):
        if not outputs:
            return {}

        temp_avg_loss_batch = [x["train_loss_batch"] for x in outputs]
        temp_avg_acc_batch = [x["train_acc_batch"] for x in outputs]

        avg_train_loss = torch.stack(temp_avg_loss_batch).mean()
        avg_train_acc = torch.stack(temp_avg_acc_batch).mean()

        self.df_performance_train_epoch = self.df_performance_train_epoch.append(
            pd.Series(
                [avg_train_loss.item(), avg_train_acc.item()],
                index=self.df_performance_train_epoch.columns,
            ),
            ignore_index=True,
        )

        tensorboard_logs = {
            "avg_train_acc": avg_train_acc,
            "avg_train_loss": avg_train_loss,
        }

        return {"avg_train_acc": avg_train_acc, "log": tensorboard_logs}

    def validation_step(self, batch, batch_nb):
        # batch
        inputs, offsets, targets = batch

        # fwd
        y_hat = self.forward(inputs, offsets)

        # loss
        loss = self.loss_funtion(y_hat, targets)

        # acc
        acc = self.get_acc(y_hat, targets)

        # constructing dataframe
        _, predicted_codes = torch.max(y_hat, dim=1)
        predicted_targets = self.label_encoder.inverse_transform(
            predicted_codes.data.cpu().numpy()
        )
        original_targets = self.label_encoder.inverse_transform(
            targets.data.cpu().numpy()
        )
        classes_probabilities = self.predict_proba(y_hat).data.cpu().numpy()

        for (
            original_target,
            target,
            predicted_target,
            predicted_code,
            classes_probability,
        ) in zip(
            original_targets,
            targets,
            predicted_targets,
            predicted_codes,
            classes_probabilities,
        ):
            
            row_info = [original_target, int(target),predicted_target,int(predicted_code)] + [prob for prob in classes_probability]
            self.df_valid = self.df_valid.append(pd.Series(row_info,index=self.df_valid.columns), ignore_index=True)

        self.df_performance_valid_batch = self.df_performance_valid_batch.append(
            pd.Series(
                [loss.item(), acc.item()], index=self.df_performance_valid_batch.columns
            ),
            ignore_index=True,
        )

        return {"valid_acc_batch": acc, "valid_loss_batch": loss}

    def validation_epoch_end(self, outputs):
        if not outputs:
            return {}
        temp_avg_loss_batch = [x["valid_loss_batch"] for x in outputs]
        temp_avg_acc_batch = [x["valid_acc_batch"] for x in outputs]

        avg_valid_loss = torch.stack(temp_avg_loss_batch).mean()
        avg_valid_acc = torch.stack(temp_avg_acc_batch).mean()

        self.df_performance_valid_epoch = self.df_performance_valid_epoch.append(
            pd.Series(
                [avg_valid_loss.item(), avg_valid_acc.item()],
                index=self.df_performance_valid_epoch.columns,
            ),
            ignore_index=True,
        )

        tensorboard_logs = {
            "avg_valid_acc": avg_valid_acc,
            "avg_valid_loss": avg_valid_loss,
        }

        return {"avg_valid_acc": avg_valid_acc, "log": tensorboard_logs}

    def test_step(self, batch, batch_nb):
        # batch
        if self.step == "Experiment":
            inputs, offsets, targets = batch
            # fwd
            y_hat = self.forward(inputs, offsets)
            # acc
            acc = self.get_acc(y_hat, targets)
            # constructing dataframe
            _, predicted_codes = torch.max(y_hat, dim=1)
            predicted_targets = self.label_encoder.inverse_transform(
                predicted_codes.data.cpu().numpy()
            )
            original_targets = self.label_encoder.inverse_transform(
                targets.data.cpu().numpy()
            )
            classes_probabilities = self.predict_proba(y_hat).data.cpu().numpy()
            for (
                original_target,
                target,
                predicted_target,
                predicted_code,
                classes_probability,
            ) in zip(
                original_targets,
                targets,
                predicted_targets,
                predicted_codes,
                classes_probabilities,
            ):
                row_info = [original_target, int(target),predicted_target,int(predicted_code)] + [prob for prob in classes_probability]
                self.df_test = self.df_test.append(pd.Series(row_info,index=self.df_test.columns), ignore_index=True)
               
            
            retorno = {"test_acc_batch": acc}

        if self.step == "Deployment":
            inputs, offsets = batch
            # fwd
            y_hat = self.forward(inputs, offsets)
            # constructing dataframe
            _, predicted_codes = torch.max(y_hat, dim=1)
            predicted_targets = self.label_encoder.inverse_transform(
                predicted_codes.data.cpu().numpy()
            )
            classes_probabilities = self.predict_proba(y_hat).data.cpu().numpy()
            not_apply_list = ["N/A"] * len(classes_probabilities)
            for not_apply, predicted_target, predicted_code, classes_probability in zip(
                not_apply_list,
                predicted_targets,
                predicted_codes,
                classes_probabilities,
            ):
                row_info = [not_apply, not_apply,predicted_target,int(predicted_code)] + [prob for prob in classes_probability]
                self.df_test = self.df_test.append(pd.Series(row_info,index=self.df_test.columns), ignore_index=True)

            retorno = None

        return retorno

    def test_epoch_end(self, outputs):
        if not outputs:
            return {}
        avg_test_acc = torch.stack([x["test_acc_batch"] for x in outputs]).mean()

        tensorboard_logs = {"avg_test_acc": avg_test_acc}

        return {"avg_test_acc": avg_test_acc, "log": tensorboard_logs}

    def configure_optimizers(self):
        return torch.optim.SGD(
            [p for p in self.parameters() if p.requires_grad], lr=self.learning_rate
        )

    def get_acc(self, y_hat, original_codes):
        _, y_hat = torch.max(y_hat, dim=1)
        val_acc = accuracy_score(y_hat.cpu(), original_codes.cpu())
        return torch.tensor(val_acc)

    def my_collate(self, batch):
        # len soma de todas as palavras
        lista_words = []
        [lista_words.extend(item[1]) for item in batch]

        # len soma de todas as palavras
        lista_words_ids = [item[0] for item in batch]
        lista_words_ids_vector = torch.cat(lista_words_ids)

        if self.step == "Experiment":
            # len batch_size
            target = [item[2] for item in batch]
            target = torch.stack(target)

        # len batch_size
        offsets = [0] + [len(entry) for entry in lista_words_ids]
        offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)

        if self.step == "Experiment":
            retorno = lista_words_ids_vector, offsets, target
        if self.step == "Deployment":
            retorno = lista_words_ids_vector, offsets

        return retorno

    def gpu_mem_restore(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                type, val, tb = sys.exc_info()
                traceback.clear_frames(tb)
                raise type(val).with_traceback(tb) from None

        return wrapper

    @gpu_mem_restore
    def train_dataloader(self):
        if self.sampler:
            targets = []
            for target in self.targets_sampler:
                targets.append(target)
            targets = torch.tensor(targets).type(torch.long)
            # Compute samples weight (each sample should get its own weight)
            class_sample_count = torch.tensor(
                [(targets == t).sum() for t in torch.unique(targets, sorted=True)]
            )
            weight = 1.0 / class_sample_count.float()
            samples_weight = torch.tensor([weight[t] for t in targets])

            # Create sampler, dataset, loader
            sampler = WeightedRandomSampler(samples_weight, len(samples_weight))
            shuffle = False
        else:
            shuffle = True
            sampler = None

        shuffle = False if self.overfit else True
        return DataLoader(
            self.train_dataset,
            sampler=sampler,
            batch_size=self.train_batch_size,
            shuffle=shuffle,
            num_workers=cpu_count(),
            collate_fn=self.my_collate,
        )

    @gpu_mem_restore
    def val_dataloader(self):
        return DataLoader(
            self.valid_dataset,
            batch_size=self.eval_batch_size,
            shuffle=False,
            num_workers=cpu_count(),
            collate_fn=self.my_collate,
        )

    @gpu_mem_restore
    def test_dataloader(self):
        return DataLoader(
            self.test_dataset,
            batch_size=self.eval_batch_size,
            shuffle=False,
            num_workers=cpu_count(),
            collate_fn=self.my_collate,
        )

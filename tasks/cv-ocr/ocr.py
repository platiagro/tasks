import pytesseract
from pytesseract import Output
import cv2 
import jiwer
import numpy as np
import pandas as pd
import base64

class Class_Pytesseract_OCR:
    def __init__(self, hyperparams,model_parameters,return_formats):
        
        #---------dataset_infos
        self.X = None
        self.y_target = None

        #---------model_parameters
        self.ocr_engine = model_parameters['ocr_engine']
        self.segmentation_mode = model_parameters['segmentation_mode']
        self.language = model_parameters['language']
        self.custom_config = self._create_custom_config_string()

        #---------hyperparams
        self.bbox_conf = hyperparams['bbox_conf']
        
        #---------return_formats
        self.bbox_return = return_formats['bbox_return']
        self.image_return_format = return_formats['image_return_format']
        self.remove_linebreaks = return_formats['remove_linebreaks']        


        #------- Results
        self.y_pred = None
        self.avg_mer = None
        self.avg_wer = None
        self.avg_wil = None
        self.avg_wip = None
        self.df_result  = None


    def _create_custom_config_string(self):
        segmentaion_mode_dict = {"Orientation and script detection (OSD) only.":"0",
                        "Automatic page segmentation with OSD.":"1",
                        "Automatic page segmentation, but no OSD, or OCR.":"2",
                        "Fully automatic page segmentation, but no OSD. (Default)":"3",
                        "Assume a single column of text of variable sizes.":"4",
                        "Assume a single uniform block of vertically aligned text.":"5",
                        "Assume a single uniform block of text.":"6",
                        "Treat the image as a single text line.":"7",
                        "Treat the image as a single word.":"8",
                        "Treat the image as a single word in a circle.":"9",
                        "Treat the image as a single character.":"10",
                        "Sparse text. Find as much text as possible in no particular order.":"11",
                        "Sparse text with OSD.":"12",
                        "Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.":"13"}

        ocr_engine_dict = {"Legacy engine only.":"0",
                  "Neural nets LSTM engine only.":"1",
                  "Legacy + LSTM engines.":"2",
                  "Default, based on what is available.":"3"}

        
        custom_config = (f"-l {self.language} --oem {ocr_engine_dict[self.ocr_engine]} --psm {segmentaion_mode_dict[self.segmentation_mode]}")
        custom_config = r'{}'.format(custom_config)

        return custom_config

    def _calc_metrics(self,ground_truth,hypothesis):
        transformation = jiwer.Compose([
            jiwer.ToLowerCase(),
            jiwer.RemoveMultipleSpaces(),
            jiwer.RemoveWhiteSpace(replace_by_space=" "),
            jiwer.SentencesToListOfWords(word_delimiter=" ")
        ]) 

        mer = jiwer.mer(
            ground_truth, 
            hypothesis, 
            truth_transform=transformation, 
            hypothesis_transform=transformation
        )

        wer = jiwer.wer(
            ground_truth, 
            hypothesis, 
            truth_transform=transformation, 
            hypothesis_transform=transformation
        )

        wil = jiwer.wil(
            ground_truth, 
            hypothesis, 
            truth_transform=transformation, 
            hypothesis_transform=transformation
        )
              
        wip = jiwer.wip(
            ground_truth, 
            hypothesis, 
            truth_transform=transformation, 
            hypothesis_transform=transformation
        )
        
        return mer,wer,wil,wip

    def _get_bounding_box(self,d):
        bboxes_list = []
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > self.bbox_conf:
                (x_min, y_min, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                x_max = x_min + w
                y_max = y_min + h
                bboxes_list.append((x_min, y_min, x_max, y_max))
        return bboxes_list
            

    def _get_metrics(self):
        mer_list,wer_list,wil_list,wip_list = [],[],[],[]
        for yt,yp in zip(self.y_target,self.y_pred):
            mer,wer,wil,wip = self._calc_metrics(yt,yp)
            mer_list.append(mer)
            wer_list.append(wer)
            wil_list.append(wil)
            wip_list.append(wip)
        return mer_list,wer_list,wil_list,wip_list, np.mean(mer_list),np.mean(wer_list),np.mean(wil_list),np.mean(wip_list)

    def _remove_linebreaks_from_text(self,text):
        if self.remove_linebreaks:
            text = text.replace("\n"," ")
            text = text.replace("\t"," ")
        return text
    
    def predict(self,img_reference,step,return_formats = None):
        if step == "Experiment":
            img = cv2.imread(img_reference)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if step == "Deployment":
            img = img_reference
            
        
        d = pytesseract.image_to_data(img, config=self.custom_config,output_type=Output.DICT)
        text = pytesseract.image_to_string(img, config=self.custom_config)
        text = self._remove_linebreaks_from_text(text)
        
        if return_formats:
            bbox_list = self._get_bounding_box(d)
            if return_formats['bbox_return'] == "np_array":
                result = bbox_list, text
            if return_formats['bbox_return'] == "image":
                img_bytes_base64  = self._overlay_image_with_bboxes(img,bbox_list,return_formats['image_return_format'])
                result = img_bytes_base64, text 
        else:
            result  = d, text       
        
        return result


    def _overlay_image_with_bboxes(self,img,bbox_list,image_type):
        for i in bbox_list:
            img = cv2.rectangle(img, (i[0], i[1]), (i[0] + i[2], i[1] + i[3]), (0, 255, 0), 2)
        
        _, buffer = cv2.imencode(image_type,img)
        img_bytes_base64 = base64.b64encode(buffer).decode()
        return img_bytes_base64
        


    def _construct_result_dataframe(self,step):
        all_bboxes_list = []
        self.y_pred = []
        for image_path in self.X:
            d,text = self.predict(image_path,step)
            text = self._remove_linebreaks_from_text(text)
            self.y_pred.append(text)
            bboxes_list = self._get_bounding_box(d)
            all_bboxes_list.append(bboxes_list)

        if step == 'Experiment':
            mer_list,wer_list,wil_list,wip_list,self.avg_mer,self.avg_wer,self.avg_wil,self.avg_wip = self._get_metrics()
            self.df_result = pd.DataFrame({'image': self.X, 'target_ocr_text': self.y_target,'predicted_ocr_text': self.y_pred,'coords(x_min,y_min,x_max,y_max)':all_bboxes_list,'match_error_rate(MER)':mer_list,'word_error_rate(WER)':wer_list,'word_information/WIL_lost(WIL)':wil_list,'word_information_preserved(WIP)':wip_list})
        
        if step == 'Deployment':
            self.df_result = pd.DataFrame({'image': self.X,'predicted_ocr_text': self.y_pred,'coords(x_min,y_min,x_max,y_max)':all_bboxes_list}) 


    def get_result_dataframe(self,X,y=None,step = 'Experiment'):

        #squeezing X if necesary
        try:
            test = X.shape[1]
            self.X = np.squeeze(X)
        except Exception as e:
            self.X = X

        #squeezing y if necesary
        try:
            test = y.shape[1] if y else 0
            self.y_target = np.squeeze(y) if y else y
        except Exception as e:
            self.y_target = y

        self._construct_result_dataframe(step)
        return self.df_result
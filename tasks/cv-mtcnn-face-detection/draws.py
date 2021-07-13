# Import Dependencies
from PIL import Image
import cv2
import numpy as np


def draw_bboxes(img_arr, bboxes, labels = None, probs = None):
    '''
    Parameters
    ----------
    img_arr : np.ndarray
        A array containing the data of a 3D image

    bboxes : np.ndarray, list
        A array of bboxes for each bbox found in the image

    labels : np.ndarray, list
        A array of labels for each bbox found in the image
        
    probs : np.ndarray, list
        A array of probabilities for each bbox found in the image

    Returns
    -------
    PIL.Image
        Returns a Image containing the bbox drawn on it, and its
        associated labels and probabilities.
    '''
    
    # Preset colors
    box_color  = (255,0,0) # red
    text_color = (0, 0, 0) # black
    
    # Image dimension size (should be square)
    img_size   = img_arr.shape[0]
    
    for bbox_id, bbox in enumerate(bboxes):
        
        # Bbox
        thickness = 2
        
        # Retrieve the start and end point
        start_point = bbox[:2].astype(np.int).tolist()
        end_point   = bbox[2:].astype(np.int).tolist()
        
        # Draw
        img_arr = cv2.rectangle(img_arr, tuple(start_point), tuple(end_point), box_color, thickness)
        
        # Labels and probs (Text)
        if labels is None and probs is None: continue
            
        if labels is not None:
            label = labels[bbox_id]
        if probs is not None:
            prob = probs[bbox_id]
        
        # Draw text box
        start_point[1] -= 20
        start_point[0] -= 1
        end_point[1]    = start_point[1] + 20
        end_point[0]   += 1
        
        img_arr = cv2.rectangle(img_arr, tuple(start_point), tuple(end_point), box_color, -1)
        
        # Draw text
        font      = cv2.FONT_HERSHEY_SIMPLEX
        pos       = [start_point[0]+5, end_point[1]-5]
        fontScale = img_size/2048
        thickness = 1
        
        if labels is not None and probs is not None:
            img_arr = cv2.putText(img_arr, f'{label}: {prob:.4f}', tuple(pos) , font, fontScale, text_color, thickness, cv2.LINE_AA)
        elif labels is not None:
            img_arr = cv2.putText(img_arr, f'{label}', tuple(pos) , font, fontScale, text_color, thickness, cv2.LINE_AA)
        else:
            img_arr = cv2.putText(img_arr, f'{prob:.4f}', tuple(pos) , font, fontScale, text_color, thickness, cv2.LINE_AA)
    
    return Image.fromarray(img_arr)

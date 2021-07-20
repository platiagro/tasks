import numpy as np

def decode_yolo_bbox(img: np.ndarray, bbox: np.ndarray):
    '''
    Transformar x, y, w, h normalizados em x_min, y_min, x_max, y_max
    '''
    
    height = img.shape[0]
    width = img.shape[1]
    
    c_x = bbox[0] * width
    c_y = bbox[1] * height
    
    half_w = (bbox[2] / 2) * width
    half_h = (bbox[3] / 2) * height
    
    bbox[0] = int(c_x - half_w)
    bbox[2] = int(c_x + half_w)
    bbox[1] = int(c_y - half_h)
    bbox[3] = int(c_y + half_h)
    
    return bbox
import colorsys
import numpy as np
import cv2
from unidecode import unidecode

# Inspired by https://github.com/hhk7734/tensorflow-yolov4

_MAX_CLASSES = 14 * 6
_HSV = [(x / _MAX_CLASSES, 1.0, 1.0) for x in range(int(_MAX_CLASSES * 1.2))]
_COLORS = [colorsys.hsv_to_rgb(*x) for x in _HSV]
_COLORS = [(int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)) for x in _COLORS]
_BBOX_COLORS = []
for i in range(_MAX_CLASSES):
    # 0 14 28 42 56 70 1 15 29 43 57 71 2 ...
    _BBOX_COLORS.append(_COLORS[14 * (i % 6) + (i // 6)])

def draw_bboxes(
    image: np.ndarray, bboxes: np.ndarray, probs: np.ndarray, names: np.ndarray
):
    """
    @parma `image`:  Dim(height, width, channel)
    @parma `bboxes`
        Dim(-1, (x_min, y_min, x_max, y_max))
    @parma `probs`
        Dim(-1,)
    @parma `names`
        Dim(-1,)
    @return drawn_image
    Usage:
        image = yolo.draw_bboxes(image, bboxes, probs, names)
    """
    height, width, _ = image.shape
    image = np.copy(image)
    name_ids = np.unique(names)

    # Draw bboxes
    for bbox_id, bbox in enumerate(bboxes):
        
        left = int(bbox[0]) # x_min
        top = int(bbox[1]) # y_min
        right = int(bbox[2]) # x_max
        bottom = int(bbox[3]) # y_max

        font_size = 0.4
        font_thickness = 1
        
        # find name id, prob and set color
        name_id = np.where(np.array(name_ids) == names[bbox_id])[0][0]
        prob = probs[bbox_id]
        color = _BBOX_COLORS[name_id%_MAX_CLASSES]

        # Get text size
        bbox_text = "{}: {:.1%}".format(names[bbox_id], prob)
        t_w, t_h = cv2.getTextSize(bbox_text, 0, font_size, font_thickness)[0]
        t_h += 3

        # Draw box
        if top < t_h:
            top = t_h
        if left < 1:
            left = 1
        if bottom >= height:
            bottom = height - 1
        if right >= width:
            right = width - 1

        cv2.rectangle(image, (left, top), (right, bottom), color, 1)

        # Draw text box
        cv2.rectangle(image, (left, top), (left + t_w, top - t_h), color, -1)

        # Draw text
        cv2.putText(
            image,
            unidecode(bbox_text), # OpenCV does not handle ~, ^, ´, etc..
            (left, top - 2),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_size,
            (
                255 - color[0],
                255 - color[1],
                255 - color[2],
            ),
            font_thickness,
            lineType=cv2.LINE_AA,
        )

    return image
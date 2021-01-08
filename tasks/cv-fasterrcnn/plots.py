from matplotlib.pyplot import cm
from sklearn.metrics import roc_curve, auc
from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np


def overlaping_multiple_plots(rows,columns,results):
    
    fig=plt.figure(figsize=(15, 15))
    ax = []
    for i in range(1, columns*rows +1):
        result = results[i]
        sample = result['image']
        sample = cv2.cvtColor(sample, cv2.COLOR_BGR2RGB)

        for pred_box in result['pred_boxes']:
            cv2.rectangle(
                sample,
                (pred_box[0], pred_box[1]),
                (pred_box[2],pred_box[3]),
                (220, 0, 0), 2
            )

        for gt_box in  result['gts_boxes']:    
            cv2.rectangle(
                sample,
                (gt_box[0], gt_box[1]),
                (gt_box[2], gt_box[3]),
                (0, 0, 220), 2
            )

        ax.append( fig.add_subplot(rows, columns, i) )
        ax[-1].set_title(result['image_id'])
        fig.suptitle("RED: Predicted | BLUE - Ground-truth")
        plt.imshow(sample)
    plt.show()
    plt.close()

    
def inference_multiple_plots(rows,columns,results):
    
    fig=plt.figure(figsize=(15, 15))
    ax = []
    for i in range(1, columns*rows +1):
        result = results[i]
        sample = result['image']
        sample = cv2.cvtColor(sample, cv2.COLOR_BGR2RGB)
        
        for pred_box in result['pred_boxes']:
            cv2.rectangle(
                sample,
                (pred_box[0], pred_box[1]),
                (pred_box[2],pred_box[3]),
                (220, 0, 0), 2
            )

        ax.append( fig.add_subplot(rows, columns, i) )
        ax[-1].set_title(result['image_id']) 
        fig.suptitle("RED: Predicted")
        plt.imshow(sample)
    plt.show()
    plt.close()

    
def performance_loss_visualization(loss_list,epoch_or_batch="Epoch",step = "Train"):
    
    x = range(len(loss_list))
    # Loss plot
    plt.xlabel(epoch_or_batch)
    plt.ylabel("Loss")
    plt.plot(x, loss_list, '-')
    plt.title(step + ' Loss Performance')
    plt.suptitle(epoch_or_batch + ' - ' + step)
    plt.show()

    
def performance_loss_iou_visualization(loss_list, iou_list,epoch_or_batch="Epoch",step = "Valid"):
    
    x = range(len(loss_list))
    # Loss plot
    plt.subplot(1, 2, 1)
    plt.xlabel(epoch_or_batch)
    plt.ylabel("Loss")
    plt.plot(x, loss_list, '-')
    plt.title(step + ' Loss Performance')
    # Precision plot
    plt.subplot(1, 2, 2)
    plt.xlabel(epoch_or_batch)
    plt.ylabel("IOU")
    plt.plot(x, iou_list, '-')
    plt.title(step + '  IOU Performance') 
    #show
    plt.subplots_adjust(wspace=0.4)
    plt.suptitle(epoch_or_batch + ' - ' + step)
    plt.show()

    
def performance_iou_visualization(iou_list,epoch_or_batch="Epoch",step = "Train"):
    
    x = range(len(iou_list))
    # Loss plot
    plt.xlabel(epoch_or_batch)
    plt.ylabel("IOU")
    plt.plot(x, iou_list, '-')
    plt.title(step + ' IOU Performance')
    plt.suptitle(epoch_or_batch + ' - ' + step)
    plt.show()
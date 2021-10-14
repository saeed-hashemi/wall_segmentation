import os, torch, PIL, torchvision.transforms
import numpy as np
import cv2
import elbow

# Function for visualizing wall prediction (original image, segmentation mask and original image with the segmented wall)
def visualize_wall(img, pred):
    img_green = img.copy()
    black_white = img.copy()
    img_green[pred == 0] = [6,255,115]
    black_white[pred == 0] = [6,255,115]
    black_white[pred != 0] = [0,0,0]
    
    
    
    elbow_point=elbow.find(pred)
    if elbow_point is not None:
        black_white[:,elbow_point[1]:][pred[:,elbow_point[1]:] == 0] = [0,0,255]
        img_green[:,elbow_point[1]:][pred[:,elbow_point[1]:] == 0] = [0,0,255]

    result = cv2.addWeighted(img_green, 0.6, img, 0.4, 0, img_green)
    im_vis = np.concatenate( (img,  black_white, result), axis = 1 )
    # PIL.Image.fromarray(im_vis).show()
    PIL.Image.fromarray(im_vis).save("Results.jpg")
    

# Function for segmenting wall in the input image
def segment_image( segmentation_module, img ):
    
    pil_to_tensor = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
            mean=[0.495, 0.505, 0.486], # These are RGB mean+std values
            std=[0.229, 0.220, 0.225])  # across a large photo dataset.
        ])
    
    img_original = np.array(img)
    img_data = pil_to_tensor(img)
    singleton_batch = {'img_data': img_data[None]}#.cuda()
    segSize = img_original.shape[:2]
    
    with torch.no_grad():
        scores = segmentation_module( singleton_batch, segSize = segSize )
    _, pred = torch.max( scores, dim = 1 )
    pred = pred.cpu()[0].numpy()
    
    visualize_wall(img_original, pred)
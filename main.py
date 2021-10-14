# System libs
import PIL.Image, numpy
# Our libs
from eval import segment_image
import infrence

segmentation_module = infrence.load(weights_encoder= 'Model weights/wall_encoder_epoch_20.pth', weights_decoder= 'Model weights/wall_decoder_epoch_20.pth')

# Testing the model on arbitrary image
image_path = 'wall.jpg' 
img = PIL.Image.open(image_path).convert('RGB')
img_original = numpy.array(img)

segment_image( segmentation_module, img )
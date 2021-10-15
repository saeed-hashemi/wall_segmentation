# wall_segmentation
<p>
<li><b>Segmentation</b></li>
I used the pretrained model in this 
I used the pre-trained model which is in this <a href="https://github.com/bjekic/WallSegmentation">repo</a> to segment the wall and generate the mask. 
  <img width="300" src="https://github.com/saeed-hashemi/wall_segmentation/blob/main/mask.jpg"/>
  <small><b>TODO:</b> For removing island masks a threshold on size can be used.</small>
  <br>
 </p>
 <p>
<li><b>Split</b></li>
To split the sided walls I used the <a href="https://github.com/saeed-hashemi/wall_segmentation/blob/main/elbow.py">elbow method</a> which calculates the distance between the top of the image and the top edge of the walls and finds the maximum distance as the conjunction point of the walls. In this method, it is supposed the image is taken in normal perspective.</p>
<img width="300" src="https://github.com/saeed-hashemi/wall_segmentation/blob/main/elbow.jpg"/>
<li><b>Visualization</b></li>
In the last step, "addWeihted" is used to overlay the colors on the original and also keep the lights and shadows effects.
</p>
The results:
<img src="https://github.com/saeed-hashemi/wall_segmentation/blob/main/Results.jpg"/>

<li><b>Test</b></li>
To test you can run the main.py by python3.

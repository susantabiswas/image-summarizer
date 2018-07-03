# Image Summarization
Image summary generation or caption generation for images using CNN-LSTM network. The model used ![MSCOCO](http://cocodataset.org/#home) dataset for training the model. The entire implementation is done in Keras.

### Model Performance on Test Images:
The model was trained for 22 epochs. The results are quite convincing.

<img src="media/1.jpg" width="430" height="490"><img src="media/2.jpg" width="430" height="490">
<img src="media/3.jpg" width="430" height="440"><img src="media/4.jpg" width="430" height="440">
<img src="media/5.jpg" width="430" height="440"><img src="media/6.jpg" width="430" height="440">
<img src="media/7.jpg">

### Model Architecture

<p align="center">
    <img src = "media/model_plot.png">
</p>

#### References:
MSCOCO dataset was downloaded from ![here](http://cocodataset.org/#home).<br>
Sparse entropy loss function bug fix from ![here](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/22_Image_Captioning.ipynb)



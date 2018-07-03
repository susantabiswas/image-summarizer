from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
import pickle 
import numpy as np
import keras
from keras.applications import InceptionV3
import os

# load the pretrained inception model in keras
image_model = InceptionV3(include_top=False)
# adding a pooling layer to make the output a 1dimensional feature vector
image_model = keras.engine.training.Model(image_model.inputs, keras.layers.GlobalAveragePooling2D()(image_model.output))

# location for extracted images
directory_loc = os.listdir('train2014/')

images = []
for filename in directory_loc:
    # read image
    img = load_img('train2014/'+filename, target_size=(229, 229))
    # convert to numpy array
    img = img_to_array(img)
    images.append(img)
    
batch_img = np.array(images)

# preprocess image
img = preprocess_input(batch_img)
# get the model predictions
pred = image_model.predict(batch_img)

with open('train_img_enc.pickle', 'wb') as f:
    pickle.dump(pred, f)
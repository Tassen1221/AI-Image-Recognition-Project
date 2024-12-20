import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras

batch_size = 32
img_height = 224
img_width = 224

class_names = ['BB','DD']

model = tf.keras.models.load_model('/Users/benjaminyang/Desktop/AI-Image-Recognition-Project/source/model/Classifier_model.keras')

sunflower_url = "https://ww2db.com/images/61af86f431b2a.jpg"
sunflower_path = tf.keras.utils.get_file('USS Iowa', origin=sunflower_url)

img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(score)

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

data_dir = "/Users/benjaminyang/Desktop/AI-Image-Recognition-Project/Ship Images"

batch_size = 32
img_height = 300
img_width = 300

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  color_mode='grayscale',
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size
)
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  color_mode='grayscale',
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size
)

class_names = train_ds.class_names

num_classes = len(class_names)

# Assuming `image` is a batch of images from train_ds
image, label = next(iter(train_ds))  # Fetch a batch of images
image = image[0]  # Extract the first image in the batch for visualization

# Display the original image
plt.imshow(image.numpy().squeeze(), cmap='gray')  # Ensure it's grayscale
plt.axis("off")
plt.show()

data_augmentation = tf.keras.Sequential([
  layers.RandomBrightness(0.2),
  layers.RandomContrast(0.2),
  layers.RandomFlip("horizontal",input_shape=(img_height,img_width,1)),
  layers.RandomRotation(0.1),
  layers.RandomZoom(0.2, fill_mode = "constant"),
  layers.RandomTranslation(0.2,0.2, fill_mode = "constant"),
])

plt.figure(figsize=(10, 10))
for i in range(9):
  augmented_image = data_augmentation(image)
  ax = plt.subplot(3, 3, i + 1)
  plt.imshow(augmented_image)
  plt.axis("off")
plt.show()

model = Sequential([
  layers.RandomBrightness(0.2),
  layers.RandomContrast(0.2),
  layers.RandomFlip("horizontal",input_shape=(img_height,img_width,1)),
  layers.RandomRotation(0.1),
  layers.RandomZoom(0.2),
  layers.RandomTranslation(0.2,0.2),
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 1)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2),
  layers.Flatten(),
  layers.Dense(64, activation='relu'),
  layers.Dense(num_classes)
])
# IMG_SHAPE = (img_height,img_width,3)
# base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
#                                                include_top=False,
#                                                weights='imagenet')

# image_batch, label_batch = next(iter(train_ds))
# feature_batch = base_model(image_batch)

# base_model.trainable = True

# # Fine-tune from this layer onwards
# fine_tune_at = 100

# # Freeze all the layers before the `fine_tune_at` layer
# for layer in base_model.layers[:fine_tune_at]:
#   layer.trainable = False

# global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
# feature_batch_average = global_average_layer(feature_batch)

# prediction_layer = tf.keras.layers.Dense(3, activation='softmax')
# prediction_batch = prediction_layer(feature_batch_average)

# inputs = tf.keras.Input(shape=(224, 224, 3))
# x = data_augmentation(inputs)
# x = base_model(x, training=False)
# x = global_average_layer(x)
# x = tf.keras.layers.Dropout(0.2)(x)
# outputs = prediction_layer(x)
# model = tf.keras.Model(inputs, outputs)

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy']
)

# initial_epochs = 30

# loss0, accuracy0 = model.evaluate(val_ds)

# print("initial loss: {:.2f}".format(loss0))
# print("initial accuracy: {:.2f}".format(accuracy0))

# history = model.fit(train_ds,
#                     epochs=initial_epochs,
#                     validation_data=val_ds)

# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']

# loss = history.history['loss']
# val_loss = history.history['val_loss']

# plt.figure(figsize=(8, 8))
# plt.subplot(2, 1, 1)
# plt.plot(acc, label='Training Accuracy')
# plt.plot(val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.ylabel('Accuracy')
# plt.ylim([min(plt.ylim()),1])
# plt.title('Training and Validation Accuracy')

# plt.subplot(2, 1, 2)
# plt.plot(loss, label='Training Loss')
# plt.plot(val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.ylabel('Cross Entropy')
# plt.ylim([0,1.0])
# plt.title('Training and Validation Loss')
# plt.xlabel('epoch')
# plt.show()

epochs=1000

history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

model.save('Classifier_model.keras')

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
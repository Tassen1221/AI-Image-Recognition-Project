import tensorflow as tf
import keras
import numpy as np
import ArraysConversion
from keras import layers
from keras.datasets import mnist
from ArraysConversion import arrays

(X_train2,y_train2),(X_test2,y_test2) = mnist.load_data()
X_train = arrays
X_train = np.array(X_train)
y_train = np.ones(70)

print(X_train.shape)

model = keras.Sequential(
    [
        tf.keras.Input(shape=(100,100)),
        layers.Flatten(),
        layers.Dense(units = 15, activation = "relu"),
        layers.Dense(units = 25, activation = "relu"),
        layers.Dense(units = 10, activation = "softmax"),
    ]
)
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X_train,y_train,
    epochs=40
)

# y_result = model.predict(X_test)
# err = 0

# for i in range(len(y_result)):
#     j = y_test[i]
#     if y_result[i][j] < 0.5:
#             err += 1
# print(err/len(y_result))
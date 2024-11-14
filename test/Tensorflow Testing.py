import tensorflow as tf
import keras
import numpy as np
import ArraysConversionBB
import ArraysConversionDD
from keras import layers
from keras.datasets import mnist
from ArraysConversionBB import arraysBB
from ArraysConversionDD import arraysDD

(X_train2,y_train2),(X_test2,y_test2) = mnist.load_data()
total_data = np.array([np.append(arraysBB, arraysDD, axis=0), np.array(np.append(np.ones(70), np.full((84,), 2), axis=0))])
(X_train,y_train) = total_data

model = keras.Sequential(
    [
        tf.keras.Input(shape=(100,100)),
        layers.Flatten(),
        layers.Dense(units = 15, activation = "relu"),
        layers.Dense(units = 25, activation = "relu"),
        layers.Dense(units = 50, activation = "relu"),
        layers.Dense(units = 10, activation = "softmax"),
    ]
)
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X_train,y_train,
    epochs=100
)

y_result = model.predict(X_train)
y_pred = np.argmax(y_result, axis=1)  # Gets the predicted class indices if using probabilities

err = 0
for i in range(len(y_pred)):
    if y_pred[i] != y_train[i]:
        err += 1

print(err / len(y_pred))
import tensorflow as tf
import keras
import numpy as np
from keras import layers
from keras.datasets import mnist

(X_train,y_train),(X_test,y_test) = mnist.load_data()

print(np.shape(X_train))

model = keras.Sequential(
    [
        tf.keras.Input(shape=(28,28)),
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

y_result = model.predict(X_test)
err = 0

for i in range(len(y_result)):
    j = y_test[i]
    if y_result[i][j] < 0.5:
            err += 1
print(err/len(y_result))
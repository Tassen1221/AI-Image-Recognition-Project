import tensorflow as tf
import keras
import numpy as np
import random
import ArraysConversionBB
import ArraysConversionDD
from keras import layers
from keras.datasets import mnist
from ArraysConversionBB import arraysBB
from ArraysConversionDD import arraysDD

k = 0
accuracy = []
while k < 20:
    X_train = np.append(arraysBB, arraysDD, axis=0)
    y_train = np.append(np.full((140,), 0), np.full((168,), 1), axis=0)
    combined = list(zip(X_train, y_train))
    random.shuffle(combined)
    X_train, y_train = zip(*combined[:250])
    X_test, y_test = zip(*combined[250:-1])
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    model = keras.Sequential(
        [
            tf.keras.Input(shape=(100,100)),
            layers.Flatten(),
            layers.Dense(units = 32, activation = "relu"),
            layers.Dense(units = 64, activation = "relu"),
            layers.Dense(units = 2, activation = "softmax"),
        ]
    )
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    )

    history = model.fit(
        X_train,y_train,
        epochs=200
    )

    y_result = model.predict(X_test)
    correct_predictions = 0

    for i in range(len(y_result)):
        predicted_class = np.argmax(y_result[i])  # Find the class with the highest probability
        if predicted_class == y_test[i]:
            correct_predictions += 1

    accuracy += [correct_predictions / len(y_test)]

    k += 1
print(np.mean(accuracy))


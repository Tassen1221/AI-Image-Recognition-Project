import tensorflow as tf
import keras
import numpy as np
import random
import ArraysConversionBB
import ArraysConversionDD
import ArraysConversionCA
from keras import layers
from keras.datasets import mnist
from ArraysConversionBB import arraysBB
from ArraysConversionDD import arraysDD

k = 0
accuracy = []
while k < 100:
    X_train = np.append(arraysBB, arraysDD, axis=0)
    y_train = np.append(np.full((2368,), 0),np.full((884,), 1), axis=0)
    combined = list(zip(X_train, y_train))
    random.shuffle(combined)
    X_train, y_train = zip(*combined[:2600])
    X_test, y_test = zip(*combined[2600:-1])
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    model = keras.Sequential(
        [
            tf.keras.Input(shape=(300,300)),
            layers.Flatten(),
            layers.Dense(units = 32, activation = "relu"),
            layers.Dense(units = 64, activation = "relu"),
            layers.Dense(units = 2, activation = "softmax"),
        ]
    )
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    )

    history = model.fit(
        X_train,y_train,
        epochs=50
    )

    y_result = model.predict(X_train)
    y_random = random_array = np.random.randint(0, 2, len(X_train))
    correct_predictions = 0
    random_correct_predictions = 0

    for i in range(len(y_result)):
        predicted_class = np.argmax(y_result[i])  # Find the class with the highest probability
        if predicted_class == y_train[i]:
            correct_predictions += 1
        if predicted_class == y_random[i]:
            random_correct_predictions += 1

    accuracy += [correct_predictions/len(y_train)]
    # accuracy += [((correct_predictions)/len(y_test))/((random_correct_predictions)/len(y_test))]
    # accuracy += [random_correct_predictions/len(y_test)]
    
    k += 1
print(np.mean(accuracy))


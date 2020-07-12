import pandas as pd
from flask import request

df = pd.read_csv('data.csv')
dataset = df.values

X = dataset[:,0:5]
Y = dataset[:,5]

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential([    Dense(32, activation='relu', input_shape=(5,)),    Dense(32, activation='relu'),    Dense(1, activation='sigmoid'),])
model.compile(optimizer='sgd',              loss='binary_crossentropy',              metrics=['accuracy'])
hist = model.fit(X_train, Y_train,          batch_size=32, epochs=100,          validation_data=(X_val, Y_val))

model.evaluate(X_test, Y_test)[0]

import matplotlib.pyplot as plt

model_2 = Sequential([    Dense(1000, activation='relu', input_shape=(5,)),    Dense(1000, activation='relu'),    Dense(1000, activation='relu'),    Dense(1000, activation='relu'),    Dense(1, activation='sigmoid'),])
model_2.compile(optimizer='adam',              loss='binary_crossentropy',              metrics=['accuracy'])
hist_2 = model_2.fit(X_train, Y_train,          batch_size=32, epochs=100,          validation_data=(X_val, Y_val))

import numpy
prediction = model_2.predict_classes(numpy.array([[28,7,5,4,1],]))
print(prediction)

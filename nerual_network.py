#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:24:16 2019

@author: trosales
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix


data1 = pd.read_csv('lenses.data', header=None, delim_whitespace = True)

data1.columns = ['col', 'age', 'prescription', 'astigmatic', 'tear rate', 'outcome']
data1 = data1.drop(columns=['col']).astype(float)

data_x = data1[['age', 'prescription', 'astigmatic', 'tear rate']]
data_y = data1[['outcome']]

#split up the data
data_train, data_test, target_train, target_test = train_test_split(
        data_x, data_y, test_size=0.30)




scaler = StandardScaler()
scaler.fit(data_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

#normalizing data??
data_train = scaler.transform(data_train)
data_test = scaler.transform(data_test)


mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(data_train, target_train)

predictions = mlp.predict(data_test)
print(confusion_matrix(target_test,predictions))
print(classification_report(target_test,predictions))
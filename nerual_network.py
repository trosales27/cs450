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


def splitAndPredict(data_x, data_y):
    
    #split up the data
    data_train, data_test, target_train, target_test = train_test_split(
         data_x, data_y, test_size=0.30)
    
    scaler = StandardScaler()
    scaler.fit(data_train)
    StandardScaler(copy=True, with_mean=True, with_std=True)
    
    #normalizing data??
    data_train = scaler.transform(data_train)
    data_test = scaler.transform(data_test)
    
    mlp = MLPClassifier(hidden_layer_sizes=(20,20,20),max_iter=500)
    mlp.fit(data_train, target_train)
    
    predictions = mlp.predict(data_test)
    print(confusion_matrix(target_test,predictions))
    print(classification_report(target_test,predictions))
    
    

#First data set: Lenses
data1 = pd.read_csv('data/lenses.data', header=None, delim_whitespace = True)

data1.columns = ['col', 'age', 'prescription', 'astigmatic', 'tear rate', 'outcome']
data1 = data1.drop(columns=['col']).astype(float)

data_x = data1[['age', 'prescription', 'astigmatic', 'tear rate']]
data_y = data1[['outcome']]

print("data1:")
splitAndPredict(data_x, data_y)



#Second data set: house-votes
data2 = pd.read_csv('data/house-votes-84.data', header=None,
                     sep=",", na_values=["?"])
 
#print(data2)
 
data2_y = data2[[0]]
data2_x = data2.drop([0], axis=1)
 
#split up the data
data_train, data_test, target_train, target_test = train_test_split(
         data_x, data_y, test_size=0.30)
 
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(data_train, target_train)
 
 
predictions = mlp.predict(data_test)
print(confusion_matrix(target_test,predictions))
print(classification_report(target_test,predictions))




#Third data set: Contraceptive Methods
data3 = pd.read_csv('data/cmc.data', header=None, sep=",")
data3.columns = ['age', 'w_ed', 'h_ed', 'num_child', 'rel', 'w_working', 
                 'h_occu', 'standard_living', 'media', 'contraceptive_method']

#print(data3)

data3_y = data3[['contraceptive_method']]
data3_x = data3.drop(columns=['contraceptive_method'])

print("data3:")
splitAndPredict(data3_x, data3_y)



#Fourth data set: images
data4 = pd.read_csv('data/segmentation.data', header=None, sep=",")
#print(data4)

data4_y = data4[[0]]
data4_x = data4.drop([0], axis=1)

print("data4:")
splitAndPredict(data4_x, data4_y)
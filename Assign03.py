#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:21:25 2019

@author: trosales
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import math
import pandas as pd

import matplotlib.pyplot as plt


#Assign03

"""
FIRST DATASET
: File: car.csv
: Car_data
"""
#read in the three data file susing pandas
#read in car.csv
names = ["buying","maint","doors","persons","lug_boot","safety", "status"]
car_data = pd.read_csv('car.csv', header=None, names=names)


#Giving string data numeric value
car_data.buying = car_data.buying.astype('category')
car_data['buying_cat'] = car_data.buying.cat.codes

car_data.maint = car_data.maint.astype('category')
car_data['maint_cat'] = car_data.maint.cat.codes

car_data.lug_boot = car_data.lug_boot.astype('category')
car_data['lug_boot_cat'] = car_data.lug_boot.cat.codes

car_data.safety = car_data.safety.astype('category')
car_data['safety_cat'] = car_data.safety.cat.codes

cleanup = {"doors": {"5more":5},
                 "persons": {"more":5}}
car_data.replace(cleanup, inplace=True)

#car_data = car_data.drop(columns=['buying', 'maint', 'lug_boot', 'safety'])

car_data = car_data[['doors', 'persons', 'buying_cat', 'maint_cat', 'lug_boot_cat',
                     'safety_cat', 'status']]

car_data.status = car_data.status.astype('category')
car_data['status_cat'] = car_data.status.cat.codes

car_target = car_data[['status_cat']]
car_data = car_data.drop(columns=['status', 'status_cat'])


#convert dataframe to numpy array
car_data = car_data.values
#print(car_data)

#.values to convert to numpy Array, ravel to convert to a 1d array
car_target = car_target.values.ravel()

#split up the data
data_train, data_test, target_train, target_test = train_test_split(
        car_data, car_target, test_size=0.30)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(data_train, target_train)
predictions = classifier.predict(data_test)

results = (predictions == target_test)

correct = 0
for i in results:
    if i == True:
        correct += 1
#print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
#      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy\n")


"""
SECOND DATASET
: File: auto-mpg.data
: mpg_data
"""
#read in auto-mpg.data
mpg_data = pd.read_csv('auto-mpg.data', header=None, delim_whitespace=True, na_values=["?"])
mpg_data.columns = ["mpg","cylinders","displacement","horsepower","weight",
                 "acceleration","modelyear","origin","carname"]

#replace unknown values with mean of column
mean = mpg_data['horsepower'].mean()
mpg_data.horsepower = mpg_data.horsepower.fillna(mean)

mpg_target = mpg_data[['mpg']]
mpg_data = mpg_data[['cylinders','displacement','horsepower','weight',
                 'acceleration','modelyear','origin']]

#Plot to a graph to see visual representation
#mpg_data['horsepower'].plot(kind='hist', bins=100)
#plt.xlabel('MPG Value')

mpg_target = mpg_target.values.ravel()
mpg_data = mpg_data.values

#split up the data
data_train, data_test, target_train, target_test = train_test_split(
        mpg_data, mpg_target, test_size=0.30)


regr = KNeighborsRegressor(n_neighbors=5)
regr.fit(data_train, target_train)
predictions = regr.predict(data_test)


results = (predictions == target_test)

correct = 0
for i in results:
    if i == True:
        correct += 1
#print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
#      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy\n")

"""
THIRD DATASET
: File: student-mat.csv
: student_data
"""
#read in student-mat.csv
student_data = pd.read_csv('student-mat.csv', sep=";")

print("Student_data is: ")
print(student_data)

#Replacing two-option values
cleanup = {"school": {"GP":0, "MS":1}, "sex": {"M":0, "F":1},
           "address": {"U":0, "R":1}, "famsize": {"GT3":0, "LE3":1},
           "Pstatus": {"A":0, "T":1}, "schoolsup": {"yes":0, "no":1},
           "famsup": {"yes":0, "no":1}, "paid": {"yes":0, "no":1}, 
           "activities": {"yes":0, "no":1}, "nursery": {"yes":0, "no":1}, 
           "higher": {"yes":0, "no":1}, "internet": {"yes":0, "no":1},
           "romantic": {"yes":0, "no":1} 
           }
student_data.replace(cleanup, inplace=True)
print("Student_data is: ")
print(student_data)


#use one-hot encoding for the remaining values
student_data = pd.get_dummies(student_data, columns=['Mjob', 'Fjob', 
                                                     'reason', 'guardian'])
print("Check 2")
print(student_data)

student_target = student_data[['G3']]
student_data = student_data.drop(columns=['G3'])

#onvert to numpy array
student_target = student_target.values.ravel()
student_data = student_data.values

#print(student_target)
#print(student_data)

#split up the data
data_train, data_test, target_train, target_test = train_test_split(
        student_data, student_target, test_size=0.30)

regr = KNeighborsRegressor(n_neighbors=5)
regr.fit(data_train, target_train)
predictions = regr.predict(data_test)


correct = 0
for i in results:
    if i == True:
        correct += 1
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy\n")


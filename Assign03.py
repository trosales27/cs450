#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:21:25 2019

@author: trosales
"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import math
import pandas as pd


#Assign03

#read in the three data file susing pandas
#read in car.csv
names = ["buying","maint","doors","persons","lug_boot","safety", "status"]
car_data = pd.read_csv('car.csv', header=None, names=names)
#print("car data is: ")
#print(car_data)

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

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(car_data, car_target)
predictions = classifier.predict(car_data)

car_target = car_target.values

car_target = car_target.ravel()
results = (predictions == car_target)

correct = 0
for i in results:
    if i == True:
        correct += 1
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")

#read in auto-mpg.data
mpg_data = pd.read_csv('auto-mpg.data', header=None, delim_whitespace=True, na_values=["?"])
mpg_data.columns = ["mpg","cylinders","displacement","horsepower","weight",
                 "acceleration","modelyear","origin","carname"]
mpg_data.horsepower = mpg_data.horsepower.fillna("unknown")
#print("mpg_data is:")




#read in student-mat.csv
student_data = pd.read_csv('student-mat.csv', sep=";", header=None)
#print("Student_data is: ")
#print(student_data)





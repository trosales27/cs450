#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:48:38 2019

@author: trosales
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
# import graphviz 

#use knn classifier
"""
KNN
: File: car.csv
: Car_data
"""

#read in car.csv
names = ["buying","maint","doors","persons","lug_boot","safety", "status"]
car_data = pd.read_csv('data/car.csv', header=None, names=names)


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
print("KNN Classifier")
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy\n")

"""
Bagging
"""
bagging = BaggingClassifier(base_estimator=classifier, max_samples=0.5, max_features=0.5)
bagging.fit(data_train, target_train)
predictions = bagging.predict(data_test)
print("\n")
print("Bagging KNN")
print(accuracy_score(target_test, predictions))


"""
Naive Bayese Algorithm??
"""
from sklearn import datasets
iris = datasets.load_iris()

data_train, data_test, target_train, target_test = train_test_split(
        iris.data, iris.target, test_size=0.30)

#training a model based off of Naive Bayes algorithm
classifier = GaussianNB()
classifier.fit(data_train, target_train)

#Make predicitons
targets_predicted = classifier.predict(data_test)

results = (targets_predicted == target_test)
correct = 0
for i in results:
    if i == True:
        correct += 1
        
print("\n")
print("GaussianNB classifier: ")
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")



"""
Decision Tree Classifier

"""
#iris = load_iris()
#clf = tree.DecisionClassifier()
#clf = clf.fit(iris.data, iris.target)
#dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("iris") 

"""
Random Forests
"""

rf = RandomForestClassifier(n_estimators=100)
rf.fit(data_train, target_train)
predictions = rf.predict(data_test)
print("\n")
print("Random forest:")
print(accuracy_score(target_test, predictions))

"""
AdaBoost
"""

ab = AdaBoostClassifier(n_estimators=100)
ab.fit(data_train, target_train)
predictions = ab.predict(data_test)
print("\n")
print("AdaBoost:")
print(accuracy_score(target_test, predictions))



# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:14:30 2019

@author: Thomas
"""
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#Load in the data
from sklearn import datasets
iris = datasets.load_iris()

# Show the data (the attributes of each instance)
print(iris.data)

# Show the target values (in numeric format) of each instance
print(iris.target)

# Show the actual target names that correspond to each number
print(iris.target_names)

#Split up the data into train and test cases
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
        
print(correct)
print(results)
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")

#Hard Coded Classifier Classer
class HardCodedClassifier:
    def fit(self, dataset_train, dataset_test):
        print("\nCalling fit method\n")    
    
    def predict(self, test_data):
        predictions = []
        for i in test_data:
            predictions.append(0)
        return predictions
            
#Applying Prediction Class
classifier = HardCodedClassifier()
classifier.fit(data_train, target_train)
targets_predicted = classifier.predict(data_test)

#Check accuracy of results
results = (targets_predicted == target_test)
correct = 0
for i in results:
    if i == True:
        correct += 1
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")

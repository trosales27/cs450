# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:14:30 2019

@author: Thomas
"""
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import math

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
        
"""print(correct)
print(results)
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")"""


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
"""results = (targets_predicted == target_test)
correct = 0
for i in results:
    if i == True:
        correct += 1
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")"""


#My own kNN class
class kNN:
    def fit(self, data_train, target_train):
        self.data_train = data_train
        self.data_test = data_test
        
    #Calculate euclidian distance
    def calculateDistance(self, x, y):
        distance = (((x[0] - y[0])**2) + 
        ((x[1] - y[1])**2) + 
        ((x[2] - y[2])**2) +
        ((x[3] - y[3])**2))
        return round(distance, 2)
                             
    #Comparing all distances and finding k number of smallest distances
    def predict(self, data_test, k):
        distances = []
        counter = 0
        for i in data_test:
            distance = self.calculateDistance(i, self.data_train[counter])
            #distances.append(distance, data_test[counter])
            tuple1 = (distance, target_test[counter])
            distances.append(tuple1)
            counter += 1
        results = [] # size k
        
        sorted_results = sorted(distances, key=lambda tup: tup[0])
        print("Sorted")
        print(sorted_results)
        i = 0
        #here need to check the most frequent number and return that
        while i < k:
            results.append(sorted_results[1][1])
            i += 1
        print("results are: ")
        print(results)
        return results
            
   
classifier = kNN()
classifier.fit(data_train, target_train)
predictions = classifier.predict(data_test, k = 3)
print("predict distances are:\n")
print(predictions) #This needs to be longer
print(target_test)
#TODO: find the classifier of the nearest neighbors, the majority of classifier will be the retunr value
results = (predictions == target_test)
correct = 0
print(results)
#for i in results:
#    if i == True:
#        correct += 1
#print("\nMy test\n")
#print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
#      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")



"""print("\nUsing existing kNN Algorithm\n")
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(data_train, target_train)
predictions = classifier.predict(data_test)
print("Actual predicitons are: \n")
print(predictions)

results = (predictions == target_test)
correct = 0
for i in results:
    if i == True:
        correct += 1
print("There were " + str(correct) + " correct estimates out of " + str(len(results)) +
      " for " + str(100 * round(correct / len(results), 2)) + "% accuracy")"""




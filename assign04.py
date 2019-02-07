#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:38:59 2019

@author: trosales
"""

import math
from collections import Counter

class decision_tree:
    
    #Needs to calculate entropy for each category
    #create branches based of the highest entropy
    
    def calcEntropy(self, data_set):

        #set data_set to an array
        data = []
        for i in data_set:
            data.append(i)
               
        print(Counter(data))
        #Make a list of the categories
        categories = Counter(data_set)

        labels = []
        for i in Counter(data):
            labels.append(i)
            
        h = 0    
        
        #This for loop begins the summation to calculate entropy for the dataset
        for i in labels:
            h += ((categories[i]/len(data)) * math.log2((categories[i]/len(data))))
            
        h *= -1
        
        print("h is:")
        print(h)
        
        
        
#testing area        
test = decision_tree()
data = ['dog', 'cat', 'dog', 'dog', 'cat', 'cat']
test.calcEntropy(data)
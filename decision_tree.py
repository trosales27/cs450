#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:52:08 2019

@author: trosales
"""
import math
from collections import Counter
from node import node

"""
:Decision Tree Class

:This will build the tree using a head node and children nodes
: enntropy for each will be calculated
: the tree will recursively build itself based off of entropy
"""
class decision_tree:
    #Needs to calculate entropy for each category
    #create branches based of the highest entropy
    
    def calcEntropy(self, data_set):
        def __init__(self, data_set):
            self.data_set = data_set
            
        #set data_set to an array
        data = []
        for i in data_set:
            data.append(i)
               
        #Make a list of just the categories
        categories = Counter(data_set)

        labels = []
        for i in Counter(data):
            labels.append(i)
            
        h = 0    
        #This for loop begins the summation to calculate entropy for the dataset
        for i in labels:
            h += ((categories[i]/len(data)) * math.log2((categories[i]/len(data))))        
        h *= -1
        
        return h
    
    def buildTree(self):
        head = node(self.data_set)
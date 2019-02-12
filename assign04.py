#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:38:59 2019

@author: trosales
"""

import math
from collections import Counter
from decision_tree import decision_tree
from node import node
import pandas as pd
from sklearn.model_selection import train_test_split

        
#testing area        
test = decision_tree()
data = ['dog', 'cat', 'dog', 'dog', 'cat', 'cat']
test.calcEntropy(data)

data1 = pd.read_csv('lenses.data', header=None, delim_whitespace = True)

data1.columns = ['col', 'age', 'prescription', 'astigmatic', 'tear rate', 'outcome']
data1 = data1.drop(columns=['col'])
print(data1)

#data_test = data1[['age', 'prescription', 'astigmatic', 'tear rate']]
#data_target = data1[['outcome']]

#split up the data
#data_train, data_test, target_train, target_test = train_test_split(
#        data_test, data_target, test_size=0.30)
head = node(data1)
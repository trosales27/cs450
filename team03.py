#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:48:35 2019

@author: trosales
"""
import pandas as pd

#read in the data from a csv file
data = pd.read_csv('adult.csv', sep=" ", header = None)
print(data)
data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
                'marital-status', 'occupation', 'relationship', 
                'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
                'native-country', 'salary']
print(data)
print((data[["workclass"]] == '?').sum())
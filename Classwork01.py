# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:01:52 2019

@author: Thomas
"""

from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
row1 = data[0]
row2 = data[1]

diff = row1 - row2
diff_squared = diff ** 2
dist = sum(diff_squared)

#dist = 0
#for i in range (len(row1)):
#    diff = row[i] - row2[i]
#    sq = diff ** 2
#    sum += sq

distances = []

#Comparing first row to all orther row distances
for row in data:
    diff = row1 - row
    diff_squared = diff ** 2
    dist = sum(diff_squared)
    distances.append(dist)


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:23:41 2018

@author: deric
"""

# Import the librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas
from apyori import apriori


# Import the dataset
store_data = pandas.read_csv("../datasets/store_data.csv", header=None)
print(store_data.head())
# Useful information
nrows = store_data.shape[0]
ncols = store_data.shape[1]

# Data Processing
records = []
for i in range(nrows):
    records.append([str(store_data.values[i,j]) for j in range(ncols)])

# Applying the apriori
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2,
                            min_lift=3, min_length=2)
association_results = list(association_rules)

# Viewing the results
print(len(association_results))
print(association_results[0])

for item in association_rules:
    
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + "->" + items[1])
    
    # Second index of the inner list
    print("Support: "+ str(item[1]))
    
    # Third index of the list located at 0th
    # of the third index of the inner list
    
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("============================================")

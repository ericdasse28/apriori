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

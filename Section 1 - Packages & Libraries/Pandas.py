# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:24:41 2023

@author: DELL
"""

import pandas as pd

# Series

s1 = pd.Series([10,20,30,40], index=['age1','age2','age3','age4'])
s2 = s1[s1>20]
s3 = s1.values
s4 = s1.index

# DataFrame

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(arr, index=['s1','s2','s3'], columns=['age1','age2','age3'])
# df2 = df
# df2['age4']=[10,11,12]
d1 = df.loc['s1']
d2 = df.loc['s1']['age2']
d3 = df.iloc[1][2] # iloc for index values
d4 = df.iloc[1,2]
d5 = df.iloc[:,0] # selecting whole rows and 0 index column
d6 = df.iloc[:,0:2]
d7 = df.drop('s2')
d8 = df.replace(2,5)
d9 = df.replace({2:5,9:8}) #replacing multiple values usind dictionaries
d10 = df.head(2)
d11 = df.tail(1)
d12 = df.sort_values('age2', ascending=False)
d13 = df.sort_index(axis=0, ascending=False)

# Reading a csv file
# data = pd.read_csv()

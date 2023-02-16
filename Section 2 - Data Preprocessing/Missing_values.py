# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:38:12 2023

@author: DELL
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)

# NaN = Not any Number
# Null = No value
# Python reports null when the cell is empty while NaN could be used when the cell that is filled with something that does not make sense.

df1 = df.info()

# Converting meaningless symbols to NaN
df2 = df.replace('!',np.NaN)
df3 = df2.info()

# Converting categorical values to numeric values
df4 = df2.apply(pd.to_numeric)

# checking for null values 
df5 = df.isnull()

# drop records with null values
df6 = df2.dropna(axis=0)

# fill null values
df7 = df2.fillna(method='ffill')

df8 = df2.columns[df2.isnull().any()]
print("Null columns are: ",df8)

# filling missing values using SimpleImputer from sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(df2)
df9 = imputer.transform(df2)
df9



# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:33:52 2023

@author: DELL
"""

import pandas as pd

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)

# renaming a column
df1 = df.rename(columns={"Temperature":"Temp"})

# deleting a column
df2 = df.drop("No. Occupants", axis=1)
df3 = df.drop("No. Occupants", axis=1, inplace=True)

# deleting a row
df4 = df.drop(2, axis=0)

# data information
df5 = df.info()

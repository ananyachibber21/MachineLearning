# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:45:27 2023

@author: DELL
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)
df_new = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_New.csv")

df2 = pd.concat([df,df_new], axis = 1)
df3 = df2.drop("No. Occupants", axis=1, inplace=True)


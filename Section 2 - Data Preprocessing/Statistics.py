# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:02:21 2023

@author: DELL
"""

import pandas as pd

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)

# describing the dataset
df1 = df.describe()

# min value from the dataset
df2 = df['E_Heat'].min()

# replacing values in a dataset
df3 = df.replace(-4,21)

# Covariance

df4 = df.cov()

# heatmap to find the correlation between the fields in dataset
import seaborn as sns
sns.heatmap(df.corr())
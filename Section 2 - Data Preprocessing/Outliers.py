# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:01:58 2023

@author: DELL
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)

df2 = df.replace('!',np.NaN)

fill = df2.fillna(method='ffill')

o1 = fill.boxplot()

# E_Plug have outliers in the plot. 
q1 = fill['E_Plug'].quantile(0.25)
q2 = fill['E_Plug'].quantile(0.75)

# q1 = 19
# q3 = 33
# iqr = q3-q1 = 33-19 = 14

# Mild Outlier
# Lower bound = q1-1.5*iqr = 19-1.5*14 = -2
# Upper Bound = q3+1.5*iqr =33+1.5*14 = 54

# Extreme Outlier
# Lower bound = q1-3*iqr = 19-3*14 = -23
# Upper Bound = q3+3*iqr = 33+3*14 = 75

# Replacing the outlier

o2 = fill['E_Plug'].replace(120,42)
# o2 = fill['E_Plug'].replace(120,42,inplace=True)



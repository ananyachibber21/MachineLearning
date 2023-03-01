# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:26:03 2023

@author: DELL
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv")
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\MachineLearning\\Dataset\\Data_Set.csv", header=2)

df2 = df.replace('!',np.NaN)

fill = df2.fillna(method='ffill')

from sklearn.preprocessing import minmax_scale, normalize

# First Method: Min Max Scale

n1 = minmax_scale(fill, feature_range=(0,1))

# Second Method: Normalization
# axis = 0 is used to normalize field | axis = 1 is used to normalize sample
# l1 is for manhattan distance | l2 is for eauclidean distance
n2 = normalize(fill, norm = 'l2', axis = 0)

# Converting the normalized array back to the DataFrame

dataF = pd.DataFrame(n2, columns=['Time','E_Plug','E_heat','Price','Temp','OffPeak'])
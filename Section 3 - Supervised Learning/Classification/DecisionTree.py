# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:38:57 2023

@author: DELL
"""

import numpy as np
import pandas as pd

# importing dataset from sklearn
from sklearn.datasets import load_iris
iris = load_iris()

# converting iris json to dataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Label'] = iris.target

x = df.iloc[:,0:4] # independent variable
y = df.iloc[:,4] # dependent variable

# Splitting the dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,
                                                 test_size=0.2, random_state=0,
                                                 shuffle=True,stratify=y)

# Training using Decision Tree
from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(x_train,y_train) 

# Prediction using test set
pred = DT.predict(x_test)

# Prediction of input array
arr = np.array([[5.3,4.1,2.5,0.6],[0.3,9.7,8.1,1.7],[1.1,2.2,3.3,7.7],
                [4.2,8.0,5.6,4.1]])
arr_df = pd.DataFrame(arr)
pred2 = DT.predict(arr_df)

# Accuracy of the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,pred)

# Cross Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(DT,x,y,cv=10)
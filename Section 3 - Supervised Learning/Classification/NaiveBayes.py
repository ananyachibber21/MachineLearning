# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:06:06 2023

@author: DELL
"""

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

# Training using Naive Bayes
from sklearn.naive_bayes import GaussianNB
NB = GaussianNB()
NB.fit(x_train,y_train)

# Prediction using test set
pred = NB.predict(x_test)

# Accuracy of the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,pred)
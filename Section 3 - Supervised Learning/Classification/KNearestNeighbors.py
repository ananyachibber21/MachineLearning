# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:02:41 2023

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset from sklearn
from sklearn.datasets import load_iris
iris = load_iris()

# converting iris json to dataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Label'] = iris.target

# Scatter Plot Visualization
plt.scatter(df.iloc[:,2], df.iloc[:,3], c = iris.target)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.show()

x = df.iloc[:,0:4] # independent variable
y = df.iloc[:,4] # dependent variable


# Splitting the dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,
                                                 test_size=0.2, random_state=0,
                                                 shuffle=True,stratify=y)

# Training using KNN
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=1) #p=1 for manhattan and p=2 for euclidean
KNN.fit(x,y) 

# Prediction using test set
pred = KNN.predict(x_test)

# Accuracy of the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,pred)

# As n_neighbors increases, the accuracy decreses.

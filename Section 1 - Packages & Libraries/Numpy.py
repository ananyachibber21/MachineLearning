# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:53:04 2023

@author: DELL
"""

import numpy as np

n1 = np.arange((8)) # Generating list of numbers using numpy
n2 = np.arange(2,6)
n3 = np.arange(2,6,2)
n4 = np.zeros((3,4))
n5 = np.ones((3,4))
n6 = np.arange(6).reshape(2,3)

#  Arrays

arr = np.array([1,2,3,4,5])
new_arr = np.array([[1,2,3],[4,5,6]])
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
m1 = matrix1@matrix2 # dot product of arrays
m3 = np.dot(matrix1,matrix2)
m2 = matrix1*matrix2 # Normal Multiplication of arrays
m4 = np.multiply(matrix1, matrix2)
m5 = matrix1 + matrix2 # Addition of arrays
m7 = np.add(matrix1,matrix2)
m6 = matrix1 - matrix2 # Subtraction of arrays
m8 = np.subtract(matrix1,matrix2)
m9 = matrix1 + 3 # Adding same number to all the values of the matrix
m10 = np.divide(matrix1,matrix2)
m11 = np.divide([5,10,15],5) # Division of arrays
m12 = np.floor_divide([5,10,15],5)
m13 = np.math.sqrt(25)

# Random Numbers

r1 = np.random.standard_normal((3,4)) # Random numbers to forma normal distribution
r2 = np.random.uniform(1,12,(3,4)) # Random Numbers to form a uniform distribution
r3 = np.random.rand() # Generate random float numbers
r4 = np.random.randint(1,50,(2,5)) # Generate random integer numbers
r5 = np.logical_and(r4>30, r4<50)
r6 = r4[r5] # Filter out the random values within the range

# Statistics

s1 = np.mean(arr)
s2 = np.median(arr)
s3 = np.var(arr)
s4 = np.std(arr)
s5 = np.var(new_arr, axis = 1)
s6 = np.var(new_arr, axis = 0)


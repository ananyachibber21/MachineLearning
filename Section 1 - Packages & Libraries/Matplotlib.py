# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:01:45 2023

@author: DELL
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

Year = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
Rate = [0,1,2,1,4,5,3,7,8,9,1]

# Line Graph

plt.plot(Year,Rate) 
plt.xlabel('Year')
plt.ylabel('Rate')
plt.title('Global Warming',{'fontsize':12, 'horizontalalignment': 'left'})
plt.show()

Month = ['Jan','Feb','March','April','May','June']
Customer1 = [2,6,4,9,1,0]
Customer2 = [4,7,4,9,3,1]
plt.plot(Month,Customer1,color='red', label='Customer 1', marker = 'o')
plt.plot(Month,Customer2,color='blue', label='Customer 2', marker = '^')
plt.xlabel('Customers')
plt.ylabel('Months')
plt.legend(loc='lower center') # To define the labels
plt.title('Months/Customers')
plt.show()

# Subplots

plt.subplot(1,2,1)
plt.plot(Month,Customer1,color='red', label='Customer 1', marker = 'o')
plt.xlabel('Customers')
plt.ylabel('Months')
plt.legend(loc='lower center') # To define the labels
plt.title('Customer A')
plt.show()

plt.subplot(1,2,2)
plt.plot(Month,Customer2,color='blue', label='Customer 2', marker = '^')
plt.xlabel('Customers')
plt.ylabel('Months')
plt.legend(loc='lower center') # To define the labels
plt.title('Customer B')
plt.show()

# Scatter Plot

plt.scatter(Month, Customer1, color='Red', label = 'Customer1')
plt.scatter(Month, Customer2, color='Blue', label = 'Customer2')
plt.xlabel('Month')
plt.ylabel('Customer')
plt.title('Scatter Plot')
plt.legend(loc='best')
plt.grid()
plt.show()

# Histogram

plt.hist(Customer1, bins=20, color='green')
plt.xlabel('Month')
plt.ylabel('Customer')
plt.title('Histogram')
plt.show()

# Bar Chart

plt.bar(Month,Customer1,width=0.8,color='blue')
plt.title('Bar Chart')
plt.show()

plt.bar(Month, Customer1, color='Red', label = 'Customer1')
plt.bar(Month, Customer2, color='Blue', label = 'Customer2')
plt.xlabel('Month')
plt.ylabel('Customer')
plt.title('Bar Plot')
plt.legend(loc='best')
plt.show()

bar_width = 0.4
Month_bar = np.arange(6)
plt.bar(Month_bar,Customer1,width=bar_width, color='blue', label='Customer1')
plt.bar(Month_bar+bar_width,Customer2,width=bar_width, color='red', label='Customer2')
plt.xlabel('Month')
plt.ylabel('Customer')
plt.title('Bar Plot')
plt.xticks(Month_bar + (bar_width)/12,('Jan','Feb','March','April','May','June'))
plt.legend(loc='best')
plt.show()

# Box plot

# plt.boxplot(Customer1)
# plt.boxplot(Customer1,notch=True) # To plot in a notch shape
# plt.boxplot(Customer1,vert=False) # To plot horizontally
# plt.boxplot(Customer1,notch=False,vert=True)

plt.boxplot([Customer1,Customer2], patch_artist=True, 
            boxprops=dict(facecolor='pink', color='red'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='blue'),
            medianprops=dict(color='yellow'))
plt.show()

q1 = np.median([3,4,12,16,32,45,56])
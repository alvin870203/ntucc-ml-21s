# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:15:19 2021

@author: Alvin
"""

import numpy as np

# In[1]
weather = ["Sunny", "Cloudy", "Raining", "Windy"]

Taipei = np.random.choice(weather, size=(4, 7), replace=True, p=[0.2, 0.5, 0.2, 0.1])  # replace: 取後放回
print(Taipei)

Hsinchu = np.random.choice(weather, size=(4, 7), replace=True, p=[0.3, 0.1, 0.1, 0.5])
print(Hsinchu)

Kaohsiung = np.random.choice(weather, size=(4, 7), replace=True, p=[0.6, 0.1, 0.1, 0.2])
print(Kaohsiung)

# In[2]
normal1 = np.random.randn(3, 5)
print(normal1)

normal2 = np.random.normal(10, 2, size=(3, 5))
print(normal2)

# In[3]
dice1 = np.random.randint(1, 7, size=15)
print(dice1)

unique1 = np.unique(dice1)
print(unique1)

unique1, count1 = np.unique(dice1, return_counts=True)
print(unique1, count1)
print(dict(zip(unique1, count1)))

# In[4]
# Homework
point2 = list(range(1,7,1))
prob2_ideal = [0.1, 0.1, 0.2, 0.1, 0.2, 0.3]
# print(point)
dice2 = np.random.choice(point2, size=(100,), replace=True, p=prob2_ideal)
print(dice2)
print(dict(zip(point2, prob2_ideal)))
unique2, count2 = np.unique(dice2, return_counts=True)
prob2_real = count2 / len(dice2)
print(dict(zip(unique2, prob2_real)))


# In[5]
slice1 = np.random.randint(20, size=20)
print(slice1)
print(slice1[:3])

slice2 = np.random.randint(20, size=(5, 5))
print(slice2)
print(slice2[:3, :3])

# In[6]
stat1 = np.arange(1, 11)
print(stat1)
print(stat1.min())
print(stat1.max())
print(stat1.sum())
print(stat1.mean())
print(stat1.std())

# In[7]
X1 = [1, 2, 3]
X2 = [10, 20, 30]
print(np.negative(X1))
print(np.add(X1, X2))
print(np.subtract(X1, X2))

# In[8]
X1 = [1, 2, 3]
X2 = [20, 36, 40]
print(np.multiply(X1, X2))
print(np.dot(X1, X2))  # return scalar
print(np.inner(X1, X2))  # return array, but print array with only one variable, the bracket will be dropped
print(np.cross(X1, X2))
print(np.outer(X1, X2))

# In[9]
X1 = [1, 2, 3]
X2 = [20, 36, 40]
print(np.divide(X1, X2))
print(np.remainder(X1, X2))

X = np.array([[1, 2], [3, 4]])
Y = np.linalg.inv(X)
print(np.dot(X, Y))  # X dot X**-1 = I

# In[10]
X1 = [1, 2, 3]  # feature1**T
X2 = [20, 36, 40]  # feature2**T
features = np.concatenate((X1, X2)).reshape(2, 3).T  # [feature1, feature2] 
print(features)

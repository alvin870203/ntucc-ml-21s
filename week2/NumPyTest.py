# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:40:02 2021

@author: Alvin
"""

import numpy as np

# In[1]
ary1 = np.array([1, 2, 3])
print(ary1)

ary2 = np.array([[1, 2, 3], [4, 5, 6]])
print(ary2)

ary3 = np.array([15, "Apple", True])
print(ary3)

# In[2]
zero1 = np.zeros((3,))
print(zero1)

zero2 = np.zeros((2, 3))
print(zero2)

identity1 = np.eye(1)
print(identity1)

identity2 = np.eye(2)
print(identity2)

one1 = np.ones((3,))
print(one1)

one2 = np.ones((2, 3))
print(one2)

const1 = np.full((3,), 7)
print(const1)

const2 = np.full((2, 3), 7)
print(const2)

# In[3]
ary1 = np.array([[1, 2, 3], [4, 5, 6]])
print(ary1[0, 0], ary1[1, 2])

ary1[0, 0] = 100
ary1[1, 2] = 600
print(ary1)

# In[4]
ary1 = np.array([[1, 2, 3], [4, 5, 6]])
print(type(ary1))
print(ary1.ndim)
print(ary1.shape)
print(ary1.dtype)

# In[5]
sample1 = np.arange(0., 5., 0.2)
print(sample1)

np.random.shuffle(sample1)
print(sample1)

sample1 = sample1.reshape(5, 5)
print(sample1)

sample1 = sample1.astype("unicode")
print(sample1)

# In[6]
sample1 = np.linspace(0., 5., 5)  # include the end
print(sample1)

sample1 = np.logspace(0., 5., 5)  # 10**i, i is linspaced
print(sample1)

# In[7]
import numpy as np

sample2 = np.random.randint(1, 7, size=15)
print(sample2)

sample3 = np.random.rand(2, 3)
print(sample3)

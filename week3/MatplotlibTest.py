# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:56:22 2021

@author: Alvin
"""

import matplotlib.pyplot as plt
import numpy as np

# In[1]
X = np.arange(0., 5., 0.2)
plt.plot(X, X, "r--")
plt.plot(X, X**2, "bs")
plt.plot(X, X**3, "g^")

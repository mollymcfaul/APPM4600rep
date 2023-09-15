#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np


# In[13]:


t = np.array(np.arange(0,math.pi,math.pi/30))


# In[15]:


y = np.cos(t)


# In[16]:


def sumvec(t,y,N):
    S = 0
    for k in range(N):
        S += t[k]*y[k]
    print(' the sum is: ', S)
sumvec(t,y,5)


# In[ ]:





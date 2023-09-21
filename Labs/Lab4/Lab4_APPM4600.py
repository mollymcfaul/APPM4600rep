#!/usr/bin/env python
# coding: utf-8

# In[48]:


# import libraries
import numpy as np
import math

def driver():

# test functions 
     f1 = lambda x: np.sqrt((10/(x+4)))
# fixed point is alpha1 = 1.4987....

    # f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,xvec,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the vector of the approximate fixed points at each iteration is:', xvec)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('Iterations:', len(xvec))
     [phatstar, phatvec] = aitkens(xvec, tol)
     print('Vector of Phats:', phatvec)
     print('Phatstar:', phatstar)
     print('Iterations:', len(phatvec))
     
#test f2 '''
#     x0 = 0.0
 #    [xstar,xvec,ier] = fixedpt(f2,x0,tol,Nmax)
  #   print('')
   #  print('the vector of the approximate fixed points at each iteration is:', xvec)  
    # print('the approximate fixed point is:',xstar)
     #print('f2(xstar):',f2(xstar))
     #print('f2(xvec):', f2(xvec))
     #print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    #xvec = np.zeros((Nmax,1))
    xvec = []
    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          xvec.append(xstar)
          return [xstar,xvec,ier]
       xvec.append(x1)
       x0 = x1
    xstar = x1
    return [xstar,xvec, ier]


def aitkens(xvec, tol):
    phatvec = []
    phat0 = 0
    for i in range(0,len(xvec)-2):
        phat1 = xvec[i] - ((xvec[i+1]-xvec[i])**2)/(xvec[i+2]-2*xvec[i+1]+xvec[i])
        if abs(phat1 - phat0)<tol:
            phatstar = phat1
            phatvec.append(phatstar)
            return[phatstar,phatvec]
        phatvec.append(phat1)
        phat0 = phat1
    phatstar = phat1
    return [phatstar, phatvec]
driver()


# In[ ]:





# In[ ]:





# In[ ]:





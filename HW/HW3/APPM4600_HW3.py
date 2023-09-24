#!/usr/bin/env python
# coding: utf-8

# In[32]:


# import libraries
import numpy as np
import math
from matplotlib import pyplot as plt 

def driver(f,tol,a,b):

# use routines    

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

  

    [astar,ier, count] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('number of iterations:', count)




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 
    count = 0
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier,count]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier,count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier,count]

    
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier,count]



# ### Problem 1 c)

# In[8]:


driver(lambda x: 2*x - np.sin(x) - 1, 0.5e-8, 0, np.pi/2)


# ```
# the approximate root is 0.8878622125563768
# the error message reads: 0
# f(astar) = 1.349093281532987e-09
# number of iterations: 28
# ```

# ### Problem 2 a) and b)

# In[9]:


driver(lambda x: (x-5)**9, 1e-4, 4.82, 5.2)


# ```
# the approximate root is 5.000073242187501
# the error message reads: 0
# f(astar) = 6.065292655789404e-38
# number of iterations: 11
# ```

# In[10]:


driver(lambda x: x**9 - 45*x**8 + 900*x**7 - 10500*x**6 + 78750*x**5 - 393750*x**4 + 1312500*x**3 - 2812500*x**2 + 3515625*x - 1953125, 1e-4, 4.82, 5.2)


# ```
# the approximate root is 5.12875
# the error message reads: 0
# f(astar) = 0.0
# number of iterations: 3
# ```

# ### Problem 3 b)

# In[31]:


driver(lambda x: x**3 + x - 4, 1e-3, 1, 4)


# ```
# the approximate root is 1.378662109375
# the error message reads: 0
# f(astar) = -0.0009021193400258198
# number of iterations: 11
# ```

# ### Problem 5

# In[38]:


x = np.arange(-2, 2*(np.pi), 0.1)
y = x - 4*np.sin(2*x) - 3
plt.title("x - 4sin(2x)-3") 
plt.xlabel("x") 
plt.ylabel("f(x)") 
plt.plot(x,y) 
plt.show()


# In[ ]:





# In[51]:


# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: -np.sin(2*x) + (5*x)/4 - 3/4
# fixed point is alpha1 = 1.4987....
 

     Nmax = 100
     tol = 0.5e-10

# test root1 '''
     x0 = -0.8
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point first is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
#test root2 '''
     x0 = -0.5
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point second is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
# test root3 '''
     x0 = 1.7
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point third is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
# test root4 '''
     x0 = 3.0
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point fourth is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
# test root5 '''
     x0 = 4.52
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point fifth is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()


# ```
# the approximate fixed point first is: -0.5444424006896952
# f1(xstar): -0.5444424006836043
# Error message reads: 0
# the approximate fixed point second is: -0.5444424006660251
# f1(xstar): -0.5444424006759575
# Error message reads: 0
# the approximate fixed point third is: -0.5444424007000309
# f1(xstar): -0.5444424006869433
# Error message reads: 0
# the approximate fixed point fourth is: 3.161826486568711
# f1(xstar): 3.1618264865393995
# Error message reads: 0
# the approximate fixed point fifth is: 69243297.18649536
# f1(xstar): 86554120.445549
# Error message reads: 1
# ```

# In[ ]:





# -*- coding: utf-8 -*-

"""
Created on Tue Jan 28 08:31:01 2020
@author: Dr. Rick Barnard (barnarr3)
modified by eya Nov 27 2021 and Dec 2021
"""

import numpy as np
 
def Beale(x):
    """
    Evaluates the Beale function and its gradient at x, a 2-vector inputted as
    a numpy array. The gradient is returned as an array. 
    """
    r = (1.5-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]**2)**2+(
            2.625-x[0]+x[0]*x[1]**3)**2
    g = np.zeros(2)
    g[0] = 2*(1.5-x[0]+x[0]*x[1])*(-1+x[1])+2*(2.25-x[0]+x[0]*x[1]**2)*(
            -1+x[1]**2)+2*(2.625-x[0]+x[0]*x[1]**3)*(-1+x[1]**3)
    g[1] = 2*(1.5-x[0]+x[0]*x[1])*(x[0])+2*(2.25-x[0]+x[0]*x[1]**2)*(
            2*x[0]*x[1])+2*(2.625-x[0]+x[0]*x[1]**3)*(3*x[0]*x[1]**2)
    return r,g

 
def Rosenbrock(x):
    """
    Evaluates the Rosenbrock function and its gradient at x.
    Technical - len() works for both lists and arrays, 
    x.size works (only) for arrays
    Parameters
    ----------
    x : TYPE n dimensional array or variable

    DESCRIPTION.  
    -----------
    Evaluates the Rosenbrock function and its gradient at x
    
    Returns
    -------
    The value of the function at x and the gradient at x as an numpy array.
    """
    n = len(x)
    r=0
    g = np.zeros(n)
    for i in range(n-1):
        r += 100*(x[i+1]-x[i]**2)**2+(1-x[i])**2
    for i in range(1,n-1):
        g[i] = -2*(1-x[i])+200*(x[i+1]-x[i]**2)*(-2*x[i])+200*(x[i]-x[i-1]**2)
    g[0] = -2*(1-x[0])+200*(x[1]-x[0]**2)*(-2*x[0])
    g[-1] = 200*(x[-1]-x[-2]**2)
    return r,g


def quadOne(x):
    """
    A quadratic with minimum at (4/7, -2/7)
    Parameters
    ----------
    x : TYPE 2D variable

    DESCRIPTION. 
    -----------
    The minimum is unique. 
    
    Returns
    -------
    The value at x and the gradient at x as an numpy array.
    """
    v = 2*x[0]**2+x[0]*x[1]+x[1]**2-2*x[0] + 1
    g = np.zeros(2)
    g[0] = 4*x[0]+x[1]-2 
    g[1] = x[0]+2*x[1]
    return v,g
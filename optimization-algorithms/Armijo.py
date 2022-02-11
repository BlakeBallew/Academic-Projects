# -*- coding: utf-8 -*-

import numpy as np
"""
Spyder Editor
created by Dr. Edoh Amiran, December 15, 2021. edoh@wwu.edu
a>0, 0<r<1, 0<c<1, p is the direction, y is f(x_k), g is the gradient
psi(a) is f(x_k+a*p), which must be available 
returns the value of a decided by the Armijo condition
"""

def armijoStep(a,r,c,p,y,g,psi):
    if (r<=0 or r>=1):
        r=0.6
    if (c<=0 or r>=1):
        c=0.0001
    b=c*np.dot(g,p)
    while(psi(a)>y+a*b):
        if(np.linalg.norm(a*p)<.01):           #quit if norm of gradient gets too small
            return a
        a=r*a
    return a


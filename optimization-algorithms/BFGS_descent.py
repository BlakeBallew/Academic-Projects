#Author: Blake Ballew
#implements Quasi-Newton method, approximating the Hessian matrix 
#via the BFGS scheme

#imports to be used in BFGS algorithm
import updateBFGS
import test_functions
import Armijo
import numpy as np
import time
import sys

"""
takes as input x and y coordinates of "starting point"
outputs numpy 1x2 array that "should" hold x and y coordinates of 
a local minimum, or at least coordinates that are sufficiently close
"""

def BFGS(x,y):
    a = .2
    r = .6
    c = .5
    tolerance = .001
    iterations = 1000
    
    def psi(a):                                          # <- psi function to be used as parameter to determine step size
        candidate = current+a*pk
        result = test_functions.Beale(candidate)[0] # <- function here will vary depending on which one we choose
        return result
    
    H = np.identity(2)                                   # <- initialize positive definite matrix to be 2x2 identity 
    current = np.array([x,y])

    for x in range(iterations):
        info = test_functions.Beale(current)        # <- info refers to the values given by the test function
        grad = info[1]                                   # as 2D list containing f(xk) and grad(f(xk)) respectively
        if np.linalg.norm(grad) < tolerance:
            print("iterations:", x)
            break

        pk = -np.dot(H,grad)                             # <- descent direction chosen per BFGS algorithm, -Hessian*grad(f(xk))

        fk = info[0]                                     # <- f evaluated at xk

        step = Armijo.armijoStep(a,r,c,pk,fk,-pk,psi)    # <- determining step size, -pk = -(-grad) = grad
        oldx = [*current]
        oldg = grad
        current += step*pk                               # <- updating current
        newg = test_functions.Beale(current)[1]     # <- finding new gradient
        cx = current-oldx                                # <- change in x_k and x_k+1
        cg = newg-oldg                                   # <- change between new and old gradients
        H = updateBFGS.bfgsUpdate(H,cg,cx)               # <- updating our positive definite Hessian approximation
    return current

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    s = time.perf_counter()
    print(BFGS(x,y))
    e = time.perf_counter()
    print("execution time: ", e-s)

if __name__ == '__main__':
        main()
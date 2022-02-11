#Author: Blake Ballew
#Gradient descent algorithm implementation (algorithm no. 2)

#imports to be used in gradient descent algorithm
import numpy as np
import Armijo
import test_functions
import time
import sys

"""
takes as input x and y coordinates of "starting point"
outputs numpy 1x2 array that "should" hold x and y coordinates of 
a local minimum, or at least coordinates that are sufficiently close
"""

def gradient_descent(x,y):
    a = .4
    r = .6
    c = .01
    tolerance = .001
    iterations = 1000

    def psi(a):                                     # <- psi function to be used as parameter to determine
        candidate = current+a*pk                    # step size in armijoStep function
        result = test_functions.Beale(candidate)[0]    # <- will vary based on which test function we're using
        return result

    current = np.array([x,y])

    for x in range(1, iterations+1):
        info = test_functions.Beale(current)   # <- info refers to the values given by the test function
        pk = -info[1]                               # <- finding new descent direction -grad(f(xk))
        
        if np.linalg.norm(pk) < tolerance:
            print("iterations", x)                  # <- if we reach our tol, break from loop and print steps needed
            break

        fk = info[0]
        step = Armijo.armijoStep(a,r,c,pk,fk,-pk,psi)  # <- we're inputting -pk as our gradient since pk itself is 
        current = current + step*pk                    # merely -grad(f(xk))
    return current  

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    s = time.perf_counter()
    print(gradient_descent(x,y))
    e = time.perf_counter()
    print("execution time: ", e-s)

if __name__ == '__main__':
        main()



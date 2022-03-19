# Author: Blake Ballew
# Description: contains functions for simulating roundabouts with various properties

from roundabout import roundabout
import matplotlib.pyplot as plt
import sys

"""
parameters:
-C is the (average or approx) time needed for a car to go around the entire roundabout
(we can think of this as containing the info for the size of the roundabout as well as the speed limit)
-S is the number of seconds we wish to simulate
-P is the probability [0,1] that if there is an open spot in the roundabout passing one of the four
inlets, there will be a car waiting there to take that spot
"""

# stuffs x-axis with values from [0,100] for P_constant since we're using X/100 as P
# [10,30] for C_constant since roundabouts rarely can be driven through in <10 seconds nor >30
# [1,S] for P_C_constant since S will be specified
def x_axis(which, S=0):
    axis = []
    if which == "P":
        for x in range(100,301):
            axis.append(x/10)
    elif which == "C":
        for x in range(1, 101):
            axis.append(x)
    else:
        for x in range(1,S+1):
            axis.append(x)
    return axis

#runs simulation and returns total flow given parameters P, C, and S
def run_sim(P, C, S):
    sim = roundabout()
    iterations = int((S/C)*4)
    for i in range(iterations):
        sim.iterate(P)
    return sim.flow

# graphs throughput (after S seconds) vs C given P in [0,1]
def P_constant(seconds, P):
    xaxis = x_axis("P")
    yaxis = []
    for x in xaxis:
        yaxis.append(run_sim(P, x, seconds))
    plt.plot(xaxis, yaxis, label = f"P={P/100}")
    plt.ylabel(f"Throughput after {seconds} seconds")
    plt.xlabel("Average Seconds to Circle Roundabout")
    plt.legend()
    plt.show()

# graphs throughput (after S seconds) vs P given C
def C_constant(seconds, C):
    xaxis = x_axis("C")
    yaxis = []
    for x in range(100):
        yaxis.append(run_sim(xaxis[x], C, seconds))
        xaxis[x] /= 100
    plt.plot(xaxis, yaxis, label=f"C={C}")
    plt.ylabel(f"Throughput after {seconds} seconds")
    plt.xlabel("Probability [0,1]")
    plt.legend()
    plt.show()

# graphs throughput vs time (in seconds) given P in [0,1] and C
def P_C_constant(seconds, P, C):
    iterations = int((seconds/(C/4)))
    xaxis = x_axis("PC", iterations)
    yaxis = []
    sim = roundabout()
    for x in range(iterations):
        sim.iterate(P)
        yaxis.append(sim.flow)
        xaxis[x] = (x*C)/4
    plt.plot(xaxis, yaxis, label=f"P={P/100}  C={C}")
    plt.ylabel("Throughput")
    plt.xlabel("Seconds passed")
    plt.legend()
    plt.show()

def main():
    args = sys.argv
    if args[1] == "P_constant":
        P_constant(int(args[2]), int(args[3]))
    elif args[1] == "C_constant":
        C_constant(int(args[2]), int(args[3]))
    else:
        P_C_constant(int(args[2]), int(args[3]), int(args[4]))



if __name__ == "__main__":
    main()
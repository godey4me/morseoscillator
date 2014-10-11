# morse.py
# Ryan Vilim, 2014
#
# This file takes in a range of initial positions and velocities (minx0-maxx0 and minx0dot-maxx0dot)
# Then solves the evolution of the Morse potential with an oscillating depth for a number (numx0 and 
# numx0dot) evenly spaced initial conditions. It then detects how long it took the particle to escape
# the well and returns an array containing this time for each initial condition 

from scipy.integrate import odeint
from pylab import *
from numpy import *
import sys

# This function defines the right hand side of the ode.
def rhs(state, t):
    x=state[0]
    
    # If our particle has escaped the well (denoted by getting to a certain value of x, escapex)
    # then record it in the escapetime array
    if (x>escapex) and (escapetime[x0index,x0dotindex]==0):
        escapetime[x0index,x0dotindex]=t
        
    # Here we are defining that the derivative of position wrt time is velocity (xdot),
    # and that the derivative of velocity (xddot) is acceleration, which equals the
    # negative gradient of the Morse potential
    xdot=state[1]
    xddot=-2*A*B*(sin(t)+2)*exp(-B*(x-1))*(1-exp(-B*(x-1)))
    
    return [xdot, xddot]

A=1
B=1

escapex=20

maxtime=200

# Get the region of parameter space to solve and how many initial conditions
# to put in that region from stdio

numx0=int(sys.argv[1])
numx0dot=int(sys.argv[4])

minx0=float(sys.argv[2])
maxx0=float(sys.argv[3])

minx0dot=float(sys.argv[5])
maxx0dot=float(sys.argv[6])

x0index=0
x0dotindex=0

t=linspace(0,maxtime,2000)

escapetime=zeros((numx0,numx0dot))
x=zeros((numx0,numx0dot))
xdot=zeros((numx0,numx0dot))

# Loop over all our initial conditions
for x0 in linspace(minx0,maxx0,num=numx0,endpoint=True):
    print (x0/maxx0)*100
    x0dotindex=0
    for x0dot in linspace(minx0dot,maxx0dot,num=numx0dot,endpoint=True):
        # Call odeint which does the business of actually solving the ode
        # this slowly builds up the "escapetime" array
        solution=odeint(rhs,[x0,x0dot],t)

        x[x0index,x0dotindex]=x0
        xdot[x0index,x0dotindex]=x0dot

        x0dotindex=x0dotindex+1
        print x0,x0dot

    x0index=x0index+1

# Save it as a compressed numpy file
savez("morse"+sys.argv[7], x=x,xdot=xdot,escapetime=escapetime)

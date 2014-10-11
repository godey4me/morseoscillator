# This file breaks the alrge region of parameter space (initial condition space)
# up into many parts, then calls morse.py to work on each of those parts. This lets
# the problem of calculating large numbers of initial conditions be parallelised on different
# computers

import os
from numpy import *
import sys

# The minimum initial x and initial xdot (velocity) that we will solve for
minx0=0
maxx0=15

minx0dot=-5
maxx0dot=5

# The total number of initial positions and velocities that we will use
numx0=15000
numx0dot=15000

# How many threads we would like to split this up into
numthreads=int(sys.argv[1])

x0 = linspace(minx0,maxx0,numx0)
i=0

# Loop over all our chunks and then call morse.py with each of them
for a in array_split(x0, numthreads):
    os.system('echo \'python morse.py '+str(size(a))+' '+str(a[0])+' '+str(a[-1])+' '+str(numx0dot)+' '+str(minx0dot)+' '+str(maxx0dot)+' '+str(i)+'\'')
    i=i+1

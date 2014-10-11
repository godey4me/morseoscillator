# This file takes all the npz fiels ouptut from morselauncher.py and morse.py and converts them
# to a matlab format. It takes in an argument about how many files we have to concatenate.

from pylab import *
import numpy as np
import scipy.io as sio

num=int(sys.argv[1])

for i in range(0,num):
    print i
    a=np.load("morse"+str(i)+".npz")["escapetime"]

    if(i!=0):
        escapetime=concatenate((escapetime,a))
    else:
        escapetime=a

sio.savemat('morse.mat', mdict={'escapetime': escapetime})

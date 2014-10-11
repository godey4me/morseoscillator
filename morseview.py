from pylab import *
import numpy as np
import Image

num=int(sys.argv[1])

for i in range(0,num):
    print i
    a=np.load("morse"+str(i)+".npz")["escapetime"]

    if(i!=0):
        escapetime=concatenate((escapetime,a))
    else:
        escapetime=a

imshow(escapetime)
show()

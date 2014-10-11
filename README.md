morseoscillator
===============

Solves the evolution of a particle in the oscillating Morse potential for a range of different initial conditions. The time it takes for each particle is recorded in a set of npz (numpy zipped) files. The number of files you get depends on how many threads you specified in morselauncher.py.

Note: The default values in morselauncher.py will generate a very large (15000x15000) set of escape times associated with those initial conditions. This may take several weeks to complete so a lower resolution or high performance computing faculties are recommended.

When the particle escapes the potential the time it took for this to happen is recorded, and the results are outputted in an npz (numpy zipped) file. 

This repository has three files

morse.py: This solves the evolution of each individual "chunk" of parameter space

morselauncher.py: This takes the whole region of parameter space, then divvies it up into many morse.py calls. This lets the problem be easily parallelised with, for example GNU parallel

morseview.py: This concatenates all the npz files output by morse.py and morselauncher.py and displays them using imshow.

matlabwrite.py: This file takes all the npz files and converts them to one matlab (.mat) file.

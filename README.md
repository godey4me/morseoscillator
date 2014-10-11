morseoscillator
===============

Solves the evolution of a particle in the Morse potential for a range of different initial conditions.

When the particle escapes the potential the time it took for this to happen is recorded, and the results are outputted in an npz (numpy zipped) file. 

This repository has three files

morse.py: This solves the evolution of each individual "chunk" of parameter space

morselauncher.py: This takes the whole region of parameter space, then divvies it up into many morse.py calls. This lets the problem be easily parallelised with, for example GNU parallel

morseview.py: This concatenates all the npz files output by morse.py and morselauncher.py and displays them using imshow.

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:37:47 2016

@author: damon
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# set data directory
data_dir = "/home/damon/gcubed/repos/cpdexample/data/"

# load contour 1 and 2
c1 = np.loadtxt(data_dir + "contour1.txt")
c2 = np.loadtxt(data_dir + "contour2.txt")


# Setup up the figure, axis and plot elements to animate
fig, ax = plt.subplots()
plt.title("affine cpd")
plt.gca().invert_yaxis()
line1, = ax.plot(c1[:,0], c1[:,1], 'b+')    # fixed target
line2, = ax.plot([], [], 'go')              # src points


# Initialization function plots the background of each frame
def init():
    line1.set_data(c1[:,0], c1[:,1])    # fixed target
    return line1, line2, line3

# Animation function which is called sequentially
def animate(i):
    print(i)
    if i == 0:
        line2.set_data(c2[:,0], c2[:,1])
    else:
        result = np.loadtxt(data_dir + "affine" + str(i) + ".txt")
        line2.set_data(result[:,0], result[:,1])
    return line1, line2, line3
        
anim = animation.FuncAnimation(fig, animate, np.arange(0,9), init_func=init)

plt.show()

## plot contours
#plt.figure()
#plt.gca().invert_yaxis()
#
#for i in range(1,9):
#
#    # load result
#    result = np.loadtxt(data_dir + "affine" + str(i) + ".txt")
#
#    # plot
#    plt.clf()
#    plt.plot(c1[:,0], c1[:,1], 'b-')
#    plt.plot(c2[:,0], c2[:,1], 'ro')
#    plt.plot(result[:,0], result[:,1], 'go')
#    
#    # pause briefly
#    plt.pause(0.5)
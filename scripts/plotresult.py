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
fig = plt.figure()

# affine subplot
plt.subplot(121)
plt.title("affine cpd")
plt.gca().invert_yaxis()
line11, = plt.plot(c1[:,0], c1[:,1], 'b+')    # fixed target
line12, = plt.plot([], [], 'go')              # src points

# nonrigid subplot
plt.subplot(122)
plt.title("nonrigid cpd")
plt.gca().invert_yaxis()
line21, = plt.plot(c1[:,0], c1[:,1], 'b+')    # fixed target
line22, = plt.plot([], [], 'go')              # src points


#fig, ax = plt.subplots()
#plt.title("affine cpd")
#plt.gca().invert_yaxis()
#line1, = ax.plot(c1[:,0], c1[:,1], 'b+')    # fixed target
#line2, = ax.plot([], [], 'go')              # src points


# Initialization function plots the background of each frame
def init():
    line11.set_data(c1[:,0], c1[:,1])    # fixed target
    line21.set_data(c1[:,0], c1[:,1])    # fixed target
    return line11, line12

# Animation function which is called sequentially
def animate(i):
    print(i)
    if i == 0:
        line12.set_data(c2[:,0], c2[:,1])
        line22.set_data(c2[:,0], c2[:,1])
    else:
        result1 = np.loadtxt(data_dir + "affine" + str(i) + ".txt")
        result2 = np.loadtxt(data_dir + "nonrigid" + str(i) + ".txt")
        line12.set_data(result1[:,0], result1[:,1])
        line22.set_data(result2[:,0], result2[:,1])
    return line11, line22
        
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
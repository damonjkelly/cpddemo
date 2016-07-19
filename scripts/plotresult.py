# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:37:47 2016

@author: damon
"""

import numpy as np
import matplotlib.pyplot as plt


# set data directory
data_dir = "/home/damon/gcubed/repos/cpdexample/"

# load contour 1
c1 = np.loadtxt(data_dir + "contour1.txt")

# load contour 2
c2 = np.loadtxt(data_dir + "contour2.txt")

# load result
result = np.loadtxt(data_dir + "result.txt")

# plot contours
plt.figure()
plt.gca().invert_yaxis()
plt.plot(c1[:,0], c1[:,1], 'b-')
plt.plot(c2[:,0], c2[:,1], 'ro')
plt.plot(result[:,0], result[:,1], 'go')
plt.show()
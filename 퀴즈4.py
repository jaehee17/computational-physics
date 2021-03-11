import numpy as np
import scipy
from numpy import sin,cos,pi

theta = (pi/9)
A = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
ex = np.array([1,0])
b = np.dot(A,ex)
print(b)
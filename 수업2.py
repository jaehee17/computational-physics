import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy import sin, cos, exp

print(sin(np.pi/2))

ex = np.array([1,0])
ey = np.array([0,1])

plt.arrow(0,0,ex[0],ex[1],head_width=0.2,color='b')
plt.arrow(0,0,ey[0],ey[1],head_width=0.2,color='r')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()
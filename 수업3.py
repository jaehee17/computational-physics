import numpy as np
import matplotlib.pyplot as plt

u = np.array([1,1])
for alpha in np.arange(-1,1,0.2):
    A = np.array([[1,alpha],[0,alpha]])
    v = np.dot(A,u)
    plt.arrow(0,0,v[0],v[1],head_width = 0.1,color='r')

plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()

A = np.array([[1,1],[0,1]])
ex = np.array([1,0])
ey = np.array([0,1])
print(np.dot(A,ex))
print(np.dot(A,ey))
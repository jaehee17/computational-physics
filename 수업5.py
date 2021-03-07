import numpy as np
#x_A = a1*t^2/2
#x_B = 100 - a2*t^2/2

#x_A = x_B -> x1*t^2/2 = 100 -x2*t^2/2, x1*t^2/2 = 100+x2*t^2/2

t1 = 30
t2 = 90

A = np.array([[(t1**2)/2,t1**2/2],[(t2**2)/2, -t2**2/2]])
b = np.array([100,100])
x = np.linalg.solve(A,b)
print('x',x)
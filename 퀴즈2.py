import numpy as np
A = np.array([[1,2],[1,-3]])
b = np.array([10,5])
x = np.linalg.solve(A,b)
print('x', x)
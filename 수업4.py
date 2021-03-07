import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],[0,3]])
Ainv = np.linalg.inv(A)
b = np.array([5,4])
print(Ainv)
print(np.dot(Ainv,b))
xsol = np.linalg.solve(A,b)
print('Sol',xsol)
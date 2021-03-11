import numpy as np
A = np.eye(1000,k=1)
B = np.eye(1000, k=0)
C = np.eye(1000, k=-1)
# 3A+2B+C가 구하려는 행렬이므로
AA = np.dot(3,A)
BB = np.dot(2,B)
print(AA+BB+C)
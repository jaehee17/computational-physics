import numpy as np
#토끼와 닭의 수:40 토끼 발:4개 닭 발: 2개 총 발 수:92개
#x = 토끼의 수
#y = 닭의 수
#x + y = 40
#4x + 2y = 92

#역행렬
A = np.array([[1,1],[4,2]])
Ainv = np.linalg.inv(A)
a = np.array([40,92])
np.dot(Ainv,a)
print(np.dot(Ainv,a))

# linalg.solve
B = np.array([[1,1],[4,2]])
b = np.array([40,92])
z = np.linalg.solve(A,a)
print ('z',z)
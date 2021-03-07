import numpy as np
import matplotlib.pyplot as plt
# A = array([a_1,b_1],[a_2,b_2])
# alpha에 따라
# alpha = 0 -> (0,1) , alpha = 1 ->(1,1), ...
# 따라서 alpha에 대해 벡터를 나타내면  v = np.array([alpha,1])
ey = np.array([0,1])
#dot(A,ey) = v -> 0(a_1)+(b_1) = alpha, 0(a_2)+(b_2) = 1
# -> b_1 = alpha b_2 = 1 a_1과 a_2는 alpha에 상관없으므로 어떤수를 넣어도됨
for alpha in np.arange(-3,3,0.5):
    A = np.array([[1,alpha],[1,1]])
    v = np.dot(A,ey)
    plt.arrow(0,0,v[0],v[1],head_width = 0.1, color='b')
plt.xlim(-5,5)
plt.ylim(-1,2)
plt.show()
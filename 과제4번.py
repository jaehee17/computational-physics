import numpy as np
#첫번째 방법
u = np.array([1,1]) 
v = np.array([1,-1])
# A = array([[a_1,b_1],[a_2,b_2]])
# dot(A,u) = [3,2] -> a_1 + b_1 = 3 , a_2 +b_2 = 2
# dot(A,v) = [-1,-2] -> a_1 - b_1 = -1 , a_2 - b_2 = -2
B = np.array([[1,1],[1,-1]])
d = np.array([3,-1])
z = np.linalg.solve(B,d)
print(z)
#a_1,b_1 구하는 연산자와 a_2,b_2구하는 연산자가 같으므로 B 그대로 사용가능
c = np.array([2,-2])
w = np.linalg.solve(B,c)
print(w)
# 따라서 a_1 = 1, b_1 = 2, a_2 =0 b_2 = 2
# A = array([1,2],[0,2])

#두번째방법
# A = array([[a_1,b_1],[a_2,b_2]])
# Au+Av = A(u+v)
Au = np.array([3,2])
Av = np.array([-1,-2])
print(u+v)
print(Au+Av)
#따라서 Au+Av = A(u+v)
#-> 2(a_1)+0(b_1)=2,  2(a_2)+0(b_2)=0 ->a_1 = 2, a_2=0
# Au-Av = A(u-v)
print(u-v)
print(Au-Av)
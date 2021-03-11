import numpy as np
a1 = np.array([2.46,0.00,0.00])
a2 = np.array([-1.23,2.14,0.00])
a3 = np.array([0.00,0.00,10.00])
#v1 = np.array([b,c,d]), v2= np.array([e,f,g]) v3 = np.array(h,i,j)
#np.dot(a1,v1) = 2.46b+0c+0d = 1
#np.dot(a2,v1) = -1.23b+2.14c+0d =0
#np.dot(a3,v1) = 0b+0c+10d = 0
#이것을 행렬로 나타내면
A = np.array([[2.46,0,0],[-1.23,2.14,0.00],[0.00,0.00,10.00]])
b1 = np.array([1,0,0])
v1 = np.linalg.solve(A,b1)
print(v1)
#위와 같은 방법으로 연립방정식을 나타내면
#np.dot(a1,v2) = 2.46e+0f+0g = 0
#np.dot(a2,v2) = -1.23e+2.14f+0g =1
#np.dot(a3,v2) = 0e+0f+10g = 0
#앞의 연산자가 같으므로 A를 써도 됨
b2 = np.array([0,1,0])
v2 = np.linalg.solve(A,b2)
print(v2)
#np.dot(a1,v3) = 2.46h+0i+0j = 0
#np.dot(a2,v3) = -1.23h+2.14i+0j =0
#np.dot(a3,v3) = 0h+0i+10j = 1
b3 = np.array([0,0,1])
v3 = np.linalg.solve(A,b3)
print(v3)
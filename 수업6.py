import numpy as np
#5v_A + 5v_B =100
#15v_A = 100 + 15v_B -> 15v_A - 15v_B =100

C = np.array([[5,5],[15,-15]])
b = ([100,100])
x = np.linalg.solve(C,b)
print(x)
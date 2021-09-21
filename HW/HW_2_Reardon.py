# E.2
import numpy as np
x = [1,2,2]
v1 = [-1,1,0]
v2 = [1,1,-2]
v3 = [1,1,0]
B = [v1,v2,v3]
B_inv = np.linalg.inv(B)
xv = B_inv
print(xv)

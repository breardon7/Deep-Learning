# E.2
import numpy as np
x = np.matrix([[1],[2],[2]])
B = np.matrix([[-1,1,1],
               [1,1,1],
               [0,-2,0]])
B_inv = np.linalg.inv(B)
xv = B_inv*x
print(xv)

# E.6

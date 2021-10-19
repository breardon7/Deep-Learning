# E.4
# iv.
import numpy as np
A = np.array([[1, 1],
               [-1,1]])
w,v = np.linalg.eigvals(A)
print('eig val: ', w)
print('eig vec: ', v)

B = np.array([1,1],
             [-np.imag,np.imag])
b_inv = np.linalg.inv(B)
print('matrix rep: ', b_inv*A*B)
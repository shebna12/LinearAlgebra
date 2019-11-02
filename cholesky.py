# https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/04LinearAlgebra/cholesky/#examples
import numpy as np
import math
from func import back_substitution,forward_substitution
# A = np.array([[25,15,-5],[15,18,0],[-5,0,11]],dtype=np.float)
A = np.array([[5,1.2,0.3,-0.6],[1.2,6,-0.4,0.9],[0.3,-0.4,8,1.7],[-0.6,0.9,1.7,10]],dtype=np.float)
b = np.array([[2.49,0.566,0.787,-2.209]],dtype=float)
m = A.shape[0]
n = A.shape[1]
L = np.zeros([m,n],dtype=np.float)

print(A)
for row_n in range(0,m):
	for col_n in range(0,row_n + 1):
		summation = np.sum([L[row_n][prev] * L[col_n][prev] for prev in range(0,col_n)])
		if(row_n == col_n):
			L[row_n][col_n] = math.sqrt(A[row_n][row_n] - summation)
		else:
			L[row_n][col_n] = (1/L[col_n][col_n] * (A[row_n][col_n] - summation))


print(L)
# 1 0 0 0 5
# 6 4 0 0 1
# 2 3 1 0 5
# 3 1 2 5 4



# Ax = b
# 1. Ly = b Forward Substitution
# 2. L^Tx = y Backward Substitution
Lb = np.concatenate((L,b.T),axis=1)
print(Lb)

y = forward_substitution(Lb)
print(np.shape(L))
print(np.shape(y.T))
Ly = np.concatenate((L,y.T[:,None]),axis=1)

print("Ly")
print(Ly)
x = back_substitution(Ly)




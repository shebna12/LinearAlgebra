# https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/04LinearAlgebra/cholesky/#examples
import numpy as np
import math
A = np.array([[25,15,-5],[15,18,0],[-5,0,11]],dtype=np.float)
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

# Ax = b
# LL^Tx = b
# L^Tx = y
# 1. Ly = b Forward Substitution
# 2. L^Tx = y Backward Substitution



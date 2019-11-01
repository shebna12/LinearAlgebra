# https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/04LinearAlgebra/cholesky/#examples
import numpy as np
import math
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
# LL^Tx = b
# L^Tx = y
# 1. Ly = b Forward Substitution
# 2. L^Tx = y Backward Substitution
Lb = np.concatenate((L,b.T),axis=1)
print(Ly)

def forward_substitution(A):
	m = np.shape(A)[0]
	n = np.shape(A)[1]
	print("{} x {}:".format(m,n))
	y = np.zeros(m,dtype=np.float)
	for i in range(0,m):
		y[i] = A[i][n-1]
		print("y[{}]: {}".format(i, y[i]))
		for j in range(0,i):
			y[i] = y[i] - (A[i][j] * y[j])
		y[i] = y[i]/A[i][i]

	print("\nRHS: ",rhs)
	return y

def back_substitution(A):
	x = np.zeros(m,dtype=np.float)
	for i in range(m-1,-1,-1):
		x[i] = A[i][n-1]
		for j in range(i+1,n-1):
			x[i] = x[i] - (A[i][j] * x[j])
	print("\nRHS: ",x)
	return x

# temp = np.array([[1,0,0,4],[1,1,0,-6],[2,-1/3,1,7]],dtype=float)
y = forward_substitution(Lb)
Ly = np.concatenate((L,y.T),axis=1)
x = back_substitution(Ly)




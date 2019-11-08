import numpy as np
import math
from func import back_substitution,forward_substitution

# Performs Cholesky Decomposition (returns L)
def cholesky(A,b):
	m = A.shape[0]
	n = A.shape[1]
	L = np.zeros([m,n],dtype=np.longdouble)
	
	for row_n in range(0,m):
		for col_n in range(0,row_n + 1):
			summation = np.sum([L[row_n][prev] * L[col_n][prev] for prev in range(0,col_n)])
			if(row_n == col_n):
				try:
					# L[row_n][col_n] = math.sqrt(A[row_n][row_n] - summation)
					L[row_n][col_n] = pow((A[row_n][row_n] - summation),0.5)
				except(ValueError):
					print("Your matrix is NOT positive definite! Program will now end...")
					import sys
					sys.exit(0)
			else:
				L[row_n][col_n] = (1/L[col_n][col_n] * (A[row_n][col_n] - summation))
	return L



# Returns the solution for Ly = b using Forward Substitution
def get_y(L,b):
	Lb = np.concatenate((L,b.T[:,None]),axis=1)
	y = forward_substitution(Lb)
	return y

# Returns the solution for L^Tx = y using Backward Substitution
def get_x(L,y):
	Ly = np.concatenate((L.T,y[:,None]),axis=1)
	x = back_substitution(Ly)
	print("Solution x: ",x)
	return x

# Returns the solution to the given linear system(Ax = b)
def get_cholesky_solution(A,b):
	L = cholesky(A,b)
	y = get_y(L,b)
	x = get_x(L,y)
	return x

if __name__ == '__main__':
	# Input
	A = np.array([[5,1.2,0.3,-0.6],[1.2,6,-0.4,0.9],[0.3,-0.4,8,1.7],[-0.6,0.9,1.7,10]],dtype=np.longdouble)
	b = np.array([2.49,0.566,0.787,-2.209],dtype=np.longdouble)
	x = get_cholesky_solution(A,b)


# Let's store all the functions here
import numpy as np

def back_substitution(A):
	m = np.shape(A)[0]
	n = np.shape(A)[1]

	x = np.zeros(m,dtype=np.float)
	for i in range(m-1,-1,-1):
		x[i] = A[i][n-1]
		for j in range(i+1,n-1):
			x[i] = x[i] - (A[i][j] * x[j])
	print("\nx: ",x)
	return x

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

	print("\ny: ",y)
	return y
import numpy as np
import fractions
import sys
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})


def forward_substitution(A,m,n):
	rhs = np.zeros(m,dtype=np.float)
	for i in range(0,m):
		rhs[i] = A[i][n-1]
		print("rhs[{}]: {}".format(i, rhs[i]))

		for j in range(0,i):
			rhs[i] = rhs[i] - (A[i][j] * rhs[j])
		rhs[i] = rhs[i]/A[i][i]
	print("\nRHS: ",rhs)

A = np.array([[1,0,0,0,5],[6,4,0,0,1],[2,3,1,0,5],[3,1,2,5,4]],dtype=float)
A = np.array([[1,0,0,2],[-1,2,0,5],[2,-1,1,9]],dtype=np.float)
m = np.shape(A)[0]
n = np.shape(A)[1]
print(A)
forward_substitution(A,m,n)
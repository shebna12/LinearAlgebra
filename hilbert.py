import numpy as np
import math
import fractions
from cholesky import get_cholesky_solution
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# Creates an nxn hilbert matrix
def hilbert_matrix(n):
	A = np.zeros((n,n),dtype=np.float64)
	# A = np.zeros((n,n),dtype=np.longdouble)

	for i in range(1,n+1):
		for j in range(1,n+1):
			A[i-1][j-1] = 1/(i+j-1)
	print("Hilbert Matrix")
	print(A)
	return A

# Returns b from (Ax=b)
def get_b(A,n):
	x = np.ones((n,1))
	b = np.dot(A,x)
	return x,b

# Returns x_prime using Cholesky's Decomposition 
def get_x_prime(A,b):
	x_prime = get_cholesky_solution(A,b.ravel())
	return x_prime

# Returns norm using Euclidean Norm
def get_norm(x,x_prime):
	euclidean_norm = math.sqrt(np.sum((x.T-x_prime)**2))
	print("Euclidean Norm")
	print(euclidean_norm)	
	return euclidean_norm

# Returns residual vector of x prime
def get_residual(b,A,x_prime):	
	r = b.T - np.dot(A,x_prime)
	print("Residuals")
	print(r)
	return r

def run_hilbert(n):
	A = hilbert_matrix(n)
	x,b = get_b(A,n)

	print("Default x: ",x.T)
	x_prime = get_x_prime(A,b)
	
	euclidean_norm = get_norm(x,x_prime)
	r = get_residual(b,A,x_prime)

if __name__ == '__main__':
	# Input 
	n = 5
	run_hilbert(n)
	
	

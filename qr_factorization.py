import numpy as np
import math
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# Performs gram_schmidt process(orthogonalization and orthonormalization)
def gram_schmidt(V,Q):
	m = np.shape(V)[0]
	n = np.shape(V)[1]
	for col_n in range(1,m):
		summation = 0
		for u_idx in range(col_n-1,-1,-1):
			summation = summation - ((np.dot(Q[u_idx],V[col_n])/np.dot(Q[u_idx],Q[u_idx]))*Q[u_idx]) 
			# print("((Q{} * V{}) / Q{} * Q{})*Q{} => {}".format(u_idx+1,col_n+1,u_idx+1,u_idx+1,u_idx+1,summation))
		Q[col_n] = V[col_n] + summation
		print("Q{}: {}".format(col_n+1,Q[col_n]))
	print("Orthogonalized Vectors")
	print(np.transpose(Q))
	Q,V = normalization(Q,m,V)

	return Q,V


# Orthonormalization process of Gram Schmidt
def normalization(Q,m,V):
    # Normalize
    for col_n in range(0,m):
        Q[col_n] = (1/math.sqrt(np.sum(Q[col_n]**2))) * Q[col_n]
    Q = Q.T
    V = V.T
    return Q,V
	

# Returns the right triangular matrix R 
def get_R(Q,V):
	# R = Q^T A
	R = np.dot(Q.T,V) ## Bitch this is working. Don't touch it na. Make docu na lang.
	print("R")
	print(R)
	return R

# Returns the solution to the given linear system
# Rx = Q^T b
def get_solution(b,R,Q,A):
	b = A.T[-1]
	R_inv_QT = np.dot(np.linalg.inv(R),Q.T)
	x = np.dot(R_inv_QT,b)

	return x

# Performs QR Factorization operations
def qr_factorization(A,b):
    A_m = np.shape(A)[0]
    A_n = np.shape(A)[1]
    V = np.transpose(A)[0:A_n-1]
    m = np.shape(V)[0]
    n = np.shape(V)[1]
    Q = np.zeros((m,n),dtype=float)
    Q[0] = V[0]

    Q,V = gram_schmidt(V,Q)
    R = get_R(Q,V)
    x = get_solution(b,R,Q,A)
    print("Solution: ",x)


if __name__ == '__main__':
    # Input
	A = np.array([[2,1,-1],[0,1/2,1/2],[-2,1,2]],dtype=np.float)
	b = np.array([8,1,-3],dtype=np.float)
	

    # Augment A and b
	Ab = np.concatenate((A,b.T[:,None]),axis=1)

	qr_factorization(Ab,b)


# http://www.seas.ucla.edu/~vandenbe/133A/lectures/lineqs.pdf
import numpy as np
import math
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# A = np.array([[2,-2,18],[2,1,0],[1,2,0]],dtype=float)
# A = np.array([[1,2,4],[0,0,5],[0,3,6]],dtype=float)
A = np.array([[2,1,0],[2,1,0],[1,5,0]],dtype=float)
# A = np.array([[-1,-1,1],[1,3,3],[-1,-1,5],[1,3,7]],dtype=float)
# A = np.array([[1,1,2,9],[2,4,-3,1],[3,6,-5,0]],dtype=np.float)
# A = np.array([[4,9,-14,0],[3,13,2,0],[0,5,0,0]],dtype=np.float)
A = np.array([[2,1,-1,8],[0,1/2,1/2,1],[-2,1,2,-3]],dtype=np.float)


print("A \n",A)
A_m = np.shape(A)[0]
A_n = np.shape(A)[1]
V = np.transpose(A)[0:A_n-1]
print("V \n",V)
m = np.shape(V)[0]
n = np.shape(V)[1]
Q = np.zeros((m,n),dtype=float)
Q[0] = V[0]

for col_n in range(1,m):
	summation = 0
	for u_idx in range(col_n-1,-1,-1):
		summation = summation - ((np.dot(Q[u_idx],V[col_n])/np.dot(Q[u_idx],Q[u_idx]))*Q[u_idx]) 
		# print("((Q{} * V{}) / Q{} * Q{})*Q{} => {}".format(u_idx+1,col_n+1,u_idx+1,u_idx+1,u_idx+1,summation))
	Q[col_n] = V[col_n] + summation
	print("Q{}: {}".format(col_n+1,Q[col_n]))
print("Orthogonalized Vectors")
print(np.transpose(Q))


# Normalize
for col_n in range(0,m):
	Q[col_n] = (1/math.sqrt(np.sum(Q[col_n]**2))) * Q[col_n]

Q = Q.T
V = V.T
print("Q Transpose")
print(Q.T)
print("V")
print(V)

# R = Q^T A
R = np.dot(Q.T,V) ## Bitch this is working. Don't touch it na. Make docu na lang.
print("R")
print(R)

b = A.T[-1]
R_inv_QT = np.dot(np.linalg.inv(R),Q.T)
print(np.dot(R_inv_QT,b))


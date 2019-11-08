import numpy as np
import math
import fractions
from cholesky import cholesky
# np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

n = 12
x = np.ones((n,1))
A = np.zeros((n,n),dtype=np.float64)
for i in range(1,n+1):
	for j in range(1,n+1):
		A[i-1][j-1] = 1/(i+j-1)
		# print("A[{},{}] = {}".format(i,j,A[i-1,j-1]))
		# print("i: ",i)
		# print("j: ",j)

print(A)
# print(x.T)
b = np.dot(A,x)
print("*******************b*********************")
print(b.T)

x_prime = cholesky(A,b.T)
# A_lol = np.concatenate((A,b),axis=1)
# print("A_lol")
# print(A_lol)
x_better_prime = np.linalg.cholesky(A)
print("X Prime")
print(x_prime)
print("X Better Prime")
print(x_better_prime)

#### Check error
# Norm
# This is ok. Already checked this.
euclidean_norm = math.sqrt(np.sum((x.T-x_prime)**2))

# errors_list = [abs(x[idx] - x_prime[idx]) for idx in range(0,n)]

r = b.T - np.dot(A,x_prime)
print("Residual")
print(r)
print("Euclidean Norm")
print(euclidean_norm)	

import numpy as np
import math
import fractions
# np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

n = 5
x = np.ones((n,1))
A = np.zeros((n,n),dtype=np.float)
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
print(b)
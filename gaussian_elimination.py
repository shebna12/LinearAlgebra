import numpy as np
import math
import fractions
import sys
from func import back_substitution
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def row_elimination_0(A,i,j):
	multiplier = -(A[i][j])/A[j][j]
	A[i][j] = multiplier * A[j][j] +  A[i][j] # This should result to 0
	for k in range(j+1,n): # Right parts should be changed too
		A[i][k] = multiplier * A[j][k] + A[i][k]
	print("\n{} * R{} + R{} -> R{} \n".format(multiplier,j+1,i+1,i+1))
	print(A)

	return A

def row_elimination_1(A,i,j):
	multiplier = 1/A[i][j] 
	# print(multiplier)
	A[i][j] = multiplier * A[i][j] # This should result to one
	# Right parts should be changed too
	for k in range(j+1,n):
		A[i][k] = multiplier * A[i][k]	

	print("\n{} * R{} -> R{}".format(multiplier,i+1,i+1))
	print(A)

	return A

def row_swapping(A,i,j):
	j_iter = j
	while(A[i][j] == 0):
		j_iter += 1
		if(j_iter < m):
			print("j_iter: ",j_iter)
			print("m:",m)
			print("Swapping")
			A[[i,j_iter]] = A[[j_iter,i]]
			print(A)
		else:
			print("Column {} has all zeroes. Singular matrix!".format(j))
			print(A)
			print("Will end now...")
			sys.exit(0)



# A = np.array([[1,1,-1,9],[0,1,3,3],[-1,0,-2,2]],dtype=np.float)
### 3x3
A = np.array([[1,1,2,9],[2,4,-3,1],[3,6,-5,0]],dtype=np.float)
A = np.array([[2,1,-1,8],[-3,0,2,-11],[-2,1,2,-3]],dtype=np.float)


### 4x4
A = np.array([[1,2,-1,1,6],[-1,1,2,-1,3],[2,-1,0,2,14],[1,1,-1,2,8]],dtype=np.float)
m = A.shape[0]
n = A.shape[1]
print("m: ",m)
print("n: ",n)

print("Original A: \n", A)
for j in range(0,n-1):
	for i in range(j,m):
		print("\n")
		# Check if pivot is zero
		if(j==i):
			if(A[i][j] == 0):
				row_swapping(A,i,j)
			elif(A[i][j] == 1):
				print("Retain")
			else: 
				A = row_elimination_1(A,i,j)
		else:
			if(A[i][j]!=0):
				A = row_elimination_0(A,i,j)
back_substitution(A)



			
import numpy as np
import math
import fractions
import sys
from func import back_substitution,forward_substitution


## Display results as fraction format
def display_as_fraction():
	np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

## Perform row operations on non-pivot elements to get 0 on left side of pivot elements.
def row_elimination_0(A,row_n,col_n,m,n):
	multiplier = -(A[row_n][col_n])/A[col_n][col_n]
	A[row_n][col_n] = multiplier * A[col_n][col_n] +  A[row_n][col_n] # This should result to 0
	for k in range(col_n+1,n): # Right parts should be changed too
		A[row_n][k] = multiplier * A[col_n][k] + A[row_n][k]
	print("\n{} * R{} + R{} -> R{} \n".format(multiplier,col_n+1,row_n+1,row_n+1))
	print(A)

	return A

## Perform row operations on pivot elements to get 1. 
def row_elimination_1(A,row_n,col_n,m,n):
	multiplier = 1/A[row_n][col_n] 
	A[row_n][col_n] = multiplier * A[row_n][col_n] # This should result to one
	# Right parts should be changed too
	for k in range(col_n+1,n):
		A[row_n][k] = multiplier * A[row_n][k]	

	print("\n{} * R{} -> R{}".format(multiplier,row_n+1,row_n+1))
	print(A)

	return A

## Swap row with pivot = 0 to a nonzero pivot by checking rows below the pivot
def row_swapping(A,row_n,col_n):
	j_iter = col_n
	while(A[row_n][col_n] == 0):
		j_iter += 1
		if(j_iter < m):
			print("j_iter: ",j_iter)
			print("m:",m)
			print("Swapping")
			A[[row_n,j_iter]] = A[[j_iter,row_n]]
			print(A)
		else:
			print("Column {} has all zeroes. Singular matrix!".format(col_n))
			print(A)
			print("Will end now...")
			sys.exit(0)

# Perform gaussian elimination method (returns solution for Ax=b)
def gaussian_elimination(A):
	m = A.shape[0]
	n = A.shape[1]
	for col_n in range(0,n-1):
		for row_n in range(col_n,m):
			print("\n")
			# Check if pivot is zero
			if(col_n==row_n):
				if(A[row_n][col_n] == 0):
					row_swapping(A,row_n,col_n)
				elif(A[row_n][col_n] == 1):
					print("Retain")
				else: 
					A = row_elimination_1(A,row_n,col_n,m,n)
			else:
				if(A[row_n][col_n]!=0):
					A = row_elimination_0(A,row_n,col_n,m,n)
	x = back_substitution(A)
	print("Solution: ",x)
	return x

if __name__ == '__main__':
	## Sample 3x3 input
	A = np.array([[2,1,-1],[-3,0,2],[-2,1,2]],dtype=np.float64)
	b = np.array([8,-11,-3],dtype=np.float64)
	
	## Sample 4x4 input
	# A = np.array([[1,2,-1,1],[-1,1,2,-1],[2,-1,0,2],[1,1,-1,2]],dtype=np.float64)
	# b = np.array([6,3,14,8],dtype=np.float64)
	
	
	# Unomment this if you want fraction version
	# display_as_fraction()


	Ab = np.concatenate((A,b.T[:,None]),axis=1)
	x = gaussian_elimination(Ab)


	



			
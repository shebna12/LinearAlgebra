# Sources:
# 	https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/04LinearAlgebra/cholesky/#examples
import numpy as np
import math
from func import back_substitution,forward_substitution
# A = np.array([[25,15,-5],[15,18,0],[-5,0,11]],dtype=np.longdouble)

def cholesky2(A,b):
    m = A.shape[0]
    n = A.shape[1]
    L = np.zeros([m,n],dtype=np.longdouble)
    np.savetxt("fee.csv", L, delimiter=",")

    for col_n in range(0,n):
        for prior_col in range(0,col_n -1):
            for row_n in range(col_n,n):
                
                # print("prior_col: ",prior_col)
                # print("col_n: ",col_n)
                A[row_n][col_n] = A[row_n][col_n] - A[row_n][prior_col] * A[col_n][prior_col]
        
        A[col_n][col_n] = math.sqrt(A[col_n][col_n])
        for prior_col in range (col_n+1,n):
            # print("prior_col: ",prior_col)
            # print("col_n: ",col_n)
            # print("prior_col: ",prior_col)


            A[prior_col][col_n] = A[prior_col][col_n] / A[col_n][col_n]
    L=A
    print("L")
    print(L)
    print("b.T")
    print(b.T)



    # Ax = b
    # 1. Ly = b Forward Substitution
    # 2. L^Tx = y Backward Substitution
    Lb = np.concatenate((L,b.T),axis=1)
    print("Lb")
    print(Lb)

    y = forward_substitution(Lb)
    print(np.shape(L))
    print(np.shape(y.T))
    Ly = np.concatenate((L,y.T[:,None]),axis=1)

    print("Ly")
    print(Ly)
    x = back_substitution(Ly)
    return x

if __name__ == '__main__':

    A = np.array([[5,1.2,0.3,-0.6],[1.2,6,-0.4,0.9],[0.3,-0.4,8,1.7],[-0.6,0.9,1.7,10]],dtype=np.longdouble)
    b = np.array([[2.49,0.566,0.787,-2.209]],dtype=float)
    
    A = np.array([[1,-1,2],[-1,5,-4],[2,4,6]],dtype=np.longdouble)

    m = A.shape[0]
    n = A.shape[1]
    L = np.zeros([m,n],dtype=np.longdouble)
    print(b)
    # A = np.array([[4,-2,2],[-2,2,-4],[2,-4,11]],dtype=np.longdouble)
    cholesky2(A,b)




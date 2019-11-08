import numpy as np
import math
import fractions
from gaussian_elimination import gaussian_elimination
from cholesky import get_cholesky_solution
from qr_factorization import qr_factorization
from hilbert import run_hilbert

if __name__ == '__main__':
    # Input
    A = np.array([[5,1.2,0.3,-0.6],[1.2,6,-0.4,0.9],[0.3,-0.4,8,1.7],[-0.6,0.9,1.7,10]],dtype=np.float64)
    b = np.array([2.49,0.566,0.787,-2.209],dtype=np.float64)
    size = 5
    Ab = np.concatenate((A,b.T[:,None]),axis=1)

    gaussian_elimination(Ab)
    get_cholesky_solution(A,b)
    qr_factorization(Ab,b)
    run_hilbert(size)
    
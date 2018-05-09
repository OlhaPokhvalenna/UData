from gauss_inverse import *


def norm(matrix):
    n = len(matrix)
    mtr_norm = 0
    for i in range(n):
        mtr_sum = 0
        for j in range(n):
            mtr_sum += abs(matrix[i][j])
        if mtr_sum > mtr_norm:
            mtr_norm = mtr_sum
    return mtr_norm


def errors(mtr, sol, mtr2):
    print("Errors:")
    for i in range(len(mtr)):
        print("error in x", i, " =", end=" ", sep='')
        mtr_sum = 0
        for j in range(len(mtr)):
            mtr_sum += sol[0][j] * mtr[i][j]
        print('{:>10}'.format(round(mtr2[0][i] - mtr_sum, 20).__str__()), end='\n')


def cond(matrix):
    return norm(matrix)*norm(gauss_inverse(matrix))

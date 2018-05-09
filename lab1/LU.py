from gauss_system import *
import copy
from determinant import determinant
# LU-matrixes


def main_minor(matrix, i):
    return [row[:i] for row in (matrix[:i])]


def lu_matrix(matrix_):
    if determinant(matrix_) == 0:
        raise ValueError("Matrix is singular")
    n = len(matrix_)
    for i in range(2, (n+1)):
        if determinant(main_minor(matrix_, i)) == 0:
            raise Exception("One of main minor is 0. LU-decomposition is impossible")
    l_matrix = [[0.0] * n for _ in range(n)]
    u_matrix = copy.deepcopy(matrix_)
    for i in range(n):
        for j in range(i, n):
            l_matrix[j][i] = u_matrix[j][i] / u_matrix[i][i]
    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                l_matrix[j][i] = u_matrix[j][i] / u_matrix[i][i]
        for i in range(k, n):
            for j in range(k - 1, n):
                u_matrix[i][j] = u_matrix[i][j] - l_matrix[i][k - 1] * u_matrix[k - 1][j]
    result = (l_matrix, u_matrix)
    return result


def gauss_solution(matrix, b_):
    b = copy.deepcopy(b_)
    n = len(matrix)
    x = [[0 for _ in range(n)]]
    for i in range(n-1, -1, -1):
        if matrix[i][i] == 0:
            raise ValueError('Matrix is singular')
        x[0][i] = b[0][i] / matrix[i][i]
        for j in range(n-1, -1, -1):
            b[0][j] -= matrix[j][i]*x[0][i]
    return x


def solution_upper_lu(matrix, b):
    n = len(matrix)
    x = [[0 for _ in range(n)]]
    for i in range(n):
        x[0][i] = b[0][i]
        for j in range(n):
            b[0][j] -= matrix[j][i] * x[0][i]
    return x


def get_y(matrix_, b):
    # Ly=b
    l_matrix = copy.deepcopy(matrix_)
    y = solution_upper_lu(l_matrix, b)
    return y


def get_x(matrix_, y_):
    # Ux=y
    u_matrix = copy.deepcopy(matrix_)
    y = copy.deepcopy(y_)
    x = gauss_solution(u_matrix, y)
    return x


def lu_solution(matrix_, b_):
    matrix = copy.deepcopy(matrix_)
    b = copy.deepcopy(b_)
    lu = lu_matrix(matrix)
    y = get_y(lu[0], b)
    x = get_x(lu[1], y)
    return x


def lu_inverse(matrix_):
    if determinant(matrix_) == 0:
        raise ValueError("Matrix is singular")
    matrix = copy.deepcopy(matrix_)
    inverse_matrix = []
    n = len(matrix[0])
    for i in range(n):
        b = [[0 for _ in range(n)]]
        b[0][i] = 1
        x = lu_solution(matrix, b)
        inverse_matrix.append(x[0])
    return inverse_matrix

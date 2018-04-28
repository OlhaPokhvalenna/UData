from determinant import*


def gauss_inverse(matrix_):
    matrix = copy.deepcopy(matrix_)
    n = len(matrix)

    # is matrix singular
    if determinant(matrix) == 0:
        raise ValueError('Matrix is singular')

    # add matrix E
    for i in range(n):
        for j in range(n):
            matrix[i].append(0)
    for i in range(n):
        matrix[i][n+i] = 1

    # first part of matrix to triangle matrix
    for k in range(n):
        for j in range(k + 1, n):
            if matrix[k][k] == 0:
                pass
            else:
                q = matrix[j][k] / matrix[k][k]
                for m in range(k, n*2):
                    matrix[j][m] -= q * matrix[k][m]

    # first part of matrix to diagonal matrix
    for k in range(n-1, -1, -1):
        for j in range(k):
            if matrix[k][k] == 0:
                pass
            else:
                q = matrix[j][k] / matrix[k][k]
                for m in range(n*2):
                    matrix[j][m] -= q * matrix[k][m]

    # first part of matrix to E-matrix, second type of matrix is inverse
    for k in range(n):
        for i in range(n*2-1, -1, -1):
            if matrix[k][k] != 0:
                matrix[k][i] = matrix[k][i]/matrix[k][k]

    # copy inverse matrix to variable inverse
    inverse = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            inverse[i][j] = matrix[i][n+j]

    return inverse

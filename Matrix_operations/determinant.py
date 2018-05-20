import copy


def determinant(matrix_):
    matrix = copy.deepcopy(matrix_)
    if len(matrix) != len(matrix[0]):
            raise IOError("Matrix is not square!!!")
    det = 1

    # matrix to triangle matrix
    for k in range(len(matrix)):
        for i in range(k, len(matrix)):
            if abs(matrix[i][k]) > abs(matrix[k][k]):
                det *= -1
                matrix[k], matrix[i] = matrix[i], matrix[k]
        for j in range(k + 1, len(matrix)):
            if matrix[k][k] == 0:
                det = 0
                break
            else:
                q = matrix[j][k] / matrix[k][k]
                for m in range(k, len(matrix)):
                    matrix[j][m] -= q * matrix[k][m]

    # det=multiple of giagonal elements
    for i in range(0, len(matrix)):
        det *= matrix[i][i]

    return det

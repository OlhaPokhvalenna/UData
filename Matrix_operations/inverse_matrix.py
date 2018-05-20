from determinant import*


def minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def transpose_matrix(matrix_):
    matrix = copy.deepcopy(matrix_)
    for i in range(len(matrix_)):
        for j in range(len(matrix_)):
            matrix[i][j] = matrix_[j][i]
    return matrix


def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular!")
    else:
        cofactors = []

        # matrix of cofactors
        for i in range(len(matrix)):
            cofactor_row = []
            for j in range(len(matrix)):
                minor_ = minor(matrix, i, j)
                cofactor_row.append(((-1) ** (i + j)) * determinant(minor_))
            cofactors.append(cofactor_row)
        cofactors = transpose_matrix(cofactors)

        # every element devide determinant of main matrix
        for j in range(len(cofactors)):
            for i in range(len(cofactors)):
                if det != 0:
                    cofactors[i][j] = cofactors[i][j] / det
        return cofactors

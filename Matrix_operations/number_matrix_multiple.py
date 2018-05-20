import copy


def multiple_number_and_matrix(matrix_, alpha):
    matrix = copy.deepcopy(matrix_)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= alpha
    return matrix

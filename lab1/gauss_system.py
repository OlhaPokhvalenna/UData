import copy


def triangle_matrix_gauss(matrix_, b_):
    matrix = copy.deepcopy(matrix_)
    b = copy.deepcopy(b_)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
        print('  |', '{:>6}'.format(round(b[0][i], 3).__str__()), end='\n')
    print('\n')

    for k in range(len(matrix)):
        for i in range(k, len(matrix)):
            if abs(matrix[i][k]) > abs(matrix[k][k]):
                matrix[k], matrix[i] = matrix[i], matrix[k]
                b[0][k], b[0][i] = b[0][i], b[0][k]
        for j in range(k + 1, len(matrix)):
            if matrix[k][k] == 0:
                pass
            else:
                q = matrix[j][k] / matrix[k][k]
                for m in range(k, len(matrix)):
                    matrix[j][m] -= q * matrix[k][m]
                b[0][j] -= q * b[0][k]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
            print('  |', '{:>6}'.format(round(b[0][i], 3).__str__()), end='\n')
        print('\n')
    return (matrix, b)


def gauss_solution(matrix, b_):
    b = copy.deepcopy(b_)
    n = len(matrix)
    x = [[0 for _ in range(n)]]
    for i in range(n-1, -1, -1):
        if matrix[i][i] == 0:
            raise ValueError('Zero division error')
        x[0][i] = b[0][i] / matrix[i][i]
        for j in range(n-1, -1, -1):
            b[0][j] -= matrix[j][i]*x[0][i]
    return x

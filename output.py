def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
        print("\n")

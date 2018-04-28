def multiple_matrixes(matrix1, matrix2):
    if len(matrix2) != len(matrix1[0]):
        raise ValueError("Multiply is not aviable")
    summ = 0
    matrix = []
    for z in range(0, len(matrix1)):
        t = []
        for j in range(0, len(matrix2[0])):
            for i in range(0, len(matrix1[0])):
                summ += matrix1[z][i] * matrix2[i][j]
            t.append(summ)
            summ = 0
        matrix.append(t)
    return matrix

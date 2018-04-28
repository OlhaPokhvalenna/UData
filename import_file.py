import numpy as np


def read_file(path):
    # read matrix
    with open(path, 'r') as file:
        matrix = file.readlines()
    matrix = [[np.round(float(n), 3) for n in x.split()] for x in matrix]

    # Check input data
    for i in range(1, (len(matrix))):
        if len(matrix[i]) != len(matrix[0]):
            raise IOError("Wrong input data!!!")

    return matrix

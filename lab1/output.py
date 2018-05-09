def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end=' ')
        print("\n")


def print_matrix_solution(matrix):
    print("Solution:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("x", j+1, sep = "", end = " =")
            print('{:>6}'.format(round(matrix[i][j], 3).__str__()), end='\n')
        print("\n")


def write_matrix(matrix, path):
    with open(path, "w") as file:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                file.write('{:>6}'.format(round(matrix[i][j], 3).__str__()))
                file.write(" ")
            file.write("\n")

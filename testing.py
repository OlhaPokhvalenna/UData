import numpy as np
from math import fabs
from gauss_inverse import*
from inverse_matrix import*


def testing():
    count_error_gauss = 0
    count_error_cofactors = 0
    amount_tests = int(input("Enter number of iterrations: "))
    eps = float(input("Enter presition (recommended 0.01): "))

    for k in range(amount_tests):
        size = np.random.randint(2, 10)
        martix = [[0.0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                martix[i][j] = np.random.randint(-10, 10)

        # is matrix singular in every method
        if np.linalg.det(np.array(martix)) == 0:
            try:
                inverse_matrix(martix)
            except ValueError:
                count_error_cofactors += 1
            try:
                gauss_inverse(martix)
            except ValueError:
                count_error_gauss += 1
            continue

        by_gauss = gauss_inverse(martix)
        by_cofactors = inverse_matrix(martix)
        by_numpy = np.linalg.inv(np.array(martix))

        is_wrong_gauss = False
        is_wrong_cofactors = False

        for i in range(size):
            for j in range(size):
                if fabs(round(by_gauss[i][j]-by_numpy[i][j], 4)) > eps:
                    is_wrong_gauss = True
                if fabs(round(by_cofactors[i][j]-by_numpy[i][j], 4)) > eps:
                    is_wrong_cofactors = True

        if is_wrong_cofactors:
            count_error_cofactors += 1
        if is_wrong_gauss:
            count_error_gauss += 1

    print("Amount of tests: ", amount_tests, sep='\n')
    print("Precision: ", eps, sep='\n')
    print("Amount of errors in Gauss-Jordan inverse method: ", count_error_gauss, sep='\n')
    print("Amount of errors in Cofactors inverse method: ", count_error_cofactors, sep='\n')


if __name__ == '__main__':
    testing()

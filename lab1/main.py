from import_file import*
from output import *
from LU import *
from norm_cond import *
from gauss_system import *


def menu():
    while True:
        print("\n\n",
              "Select operation:",
              "1:Determinant",
              "2:SLAE (LU-method)",
              "3:SLAE (Gauss method)",
              "4:Inverse matrix",
              "5: cond(matrix)",
              sep='\n')
        select = int(input())
        try:
            mtr = read_file("default.txt")
            if select == 1:
                print("\nDeterminant:")
                print(determinant(mtr), end='\n')

            elif select == 2:
                path2 = "defaultB.txt"
                mtr2 = read_file(path2)
                lu_matrix(mtr)
                print("L-matrix:")
                print_matrix(lu_matrix(mtr)[0])
                print("U-matrix")
                print_matrix(lu_matrix(mtr)[1])
                sol = lu_solution(mtr, mtr2)
                print_matrix_solution(sol)
                errors(mtr, sol, mtr2)

            elif select == 3:
                path2 = "defaultB.txt"
                mtr2 = read_file(path2)
                matrix = triangle_matrix_gauss(mtr, mtr2)
                sol = gauss_solution(matrix[0], matrix[1])
                print_matrix_solution(sol)
                errors(mtr, sol, mtr2)

            elif select == 4:
                print("LU-inverse matrix:")
                print_matrix(lu_inverse(mtr))
                print("Gauss-inverse matrix:")
                print_matrix(gauss_inverse(mtr))

            elif select == 5:
                print("cond(inf-norm):")
                print(cond(mtr))

        except Exception as e:
            print(e.args[-1])
            print("Try again!")


menu()

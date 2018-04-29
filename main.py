from gauss_inverse import *
from import_file import*
from inverse_matrix import *
from matrix_matrix_multiple import *
from number_matrix_multiple import *
from output import *


def menu():
    while True:
        print("Select operation:",
              "1:Determinant",
              "2:Inverse matrix (Gauss-Jordan method)",
              "3:Inverse matrix (Cofactors method)",
              "4:Multiple number and matrix",
              "5:Multiple matrixes",
              sep='\n')
        select = int(input())
        while True:
            path = input("Enter the way to the file with matrix:")
            try:
                mtr = read_file(path)
            except IOError:
                print("Invalid File, try again\n")
            else:
                if select == 1:
                    print("\nDeterminant:")
                    print(determinant(mtr), end='\n')
                    break
                elif select == 2:
                    print("\nInverse matrix (Gauss-Jordan method):")
                    try:
                        print_matrix(gauss_inverse(mtr))
                        path = input("Enter name of file where matrix will be written:")
                        write_matrix(gauss_inverse(mtr), path)
                    except ValueError:
                        print("Matrix is singular!")
                    break
                elif select == 3:
                    print("\nInverse matrix (Cofactors method):")
                    try:
                        print_matrix(inverse_matrix(mtr))
                        path = input("Enter name of file where matrix will be written:")
                        write_matrix(inverse_matrix(mtr), path)
                    except ValueError:
                        print("Matrix is singular!")
                    break
                elif select == 4:
                    num = float(input("\nEnter number:"))
                    print("Number*Matrix:")
                    print_matrix(multiple_number_and_matrix(mtr, num))
                    path = input("Enter name of file where matrix will be written:")
                    write_matrix(multiple_number_and_matrix(mtr, num), path)
                    break
                elif select == 5:
                    path2 = input("Enter the way to the file with second matrix:")
                    try:
                        mtr2 = read_file(path2)
                    except IOError:
                        print("\nInvalid File, try again\n")
                    else:
                        print("\nMatrix*Matrix:")
                        print_matrix(multiple_matrixes(mtr, mtr2))
                        path = input("Enter name of file where matrix will be written:")
                        write_matrix(multiple_matrixes(mtr, mtr2), path)
                    break


menu()

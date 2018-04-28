from determinant import determinant
from importFile import readFile
from inverseMatrix import inverseMatrix
from matrixMatrixMultiple import matrixMatrix
from numberMatrixMultiple import numberMatrix
import numpy as np

#OutputMatrix
def printMatrix(matrix):
    print("\nMatrix:")
    for i in range(len(matrix)):
        print(np.round(matrix[i],3))
def menu():
    while True:
        select=int(input("Select operation:\n1:determinant\n2:inverse matrix\n3:number*matrix\n4:matrix*matrix\nany other point: exit\n"))
        while True:
            path = input("Enter the way to file with matrix:")
            try: mtr = readFile(path)
            except Exception: print("Invalid File, try again\n")
            else:
                printMatrix(mtr)
                if select == 1:
                    print("Determinant:")
                    print(determinant(mtr))
                    break
                elif select==2:
                    print("Inverse matrix:")
                    printMatrix(inverseMatrix(mtr))
                    break
                elif select == 3:
                    num=input("Enter number:")
                    printMatrix(mtr)
                    print("Number*Matrix:")
                    printMatrix(numberMatrix(mtr, num))
                    break
                elif select == 4:
                    path2 = input("Enter the way to file with second matrix:")
                    try:
                        mtr2 = readFile(path2)
                    except Exception:
                        print("Invalid File, try again\n")
                    else:
                        mtr2 = readFile(path2)
                        print("Matrix*Matrix:")
                        printMatrix(matrixMatrix(mtr, mtr2))
                    break

        else:
            break


menu()
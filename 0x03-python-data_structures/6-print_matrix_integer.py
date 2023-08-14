#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = 1
        for j in i:
            if x == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            x = x + 1
        print()

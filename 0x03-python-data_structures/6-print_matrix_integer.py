#!/ust/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in (matrix):
        for j in i:
            if j is not i[len(j) - 1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()

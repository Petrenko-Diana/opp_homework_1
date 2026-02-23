def read_matrix(filename):
    matrix = []
    f = open(filename)
    for line in f:
        matrix.append([int(x) for x in line.split()])
    f.close()

def write_matrix(filename, matrix):
    f = open(filename, "w")
    for row in matrix:
        print(*row, file=f)
    f.close()

A = read_matrix("matrix.txt")
B = [
    [3, 6, 0],
    [4, 3, 1],
    [8, 2, 4]
]
write_matrix("matrix.txt", B)
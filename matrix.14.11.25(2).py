n, m = [int(x) for x in input().split()]

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

print(matrix)
for row in matrix:
    print(*row)
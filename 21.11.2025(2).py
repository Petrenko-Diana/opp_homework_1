A = [
    [int(x) for x in input().split()]
    for _ in range(3)
]

determinant = A[0][0]*A[1][1]*A[2][2] + A[1][0]*A[2][1]*A[0][2] + A[2][0]*A[0][1]*A[1][2] - A[0][2]*A[1][1]*A[2][0] - A[0][1]*A[1][0]*A[2][2] - A[1][2]*A[2][1]*A[0][0]

print(determinant)
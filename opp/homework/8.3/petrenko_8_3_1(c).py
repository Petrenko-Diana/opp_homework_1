import numpy as np

n = int(input("Введіть порядок матриці n (n >= 1): "))

if n < 1:
    print("Порядок матриці має бути >= 1.")
else:
    A = np.zeros((n, n))

    for i in range(n):
        A[i, i] = 2
        if i + 1 < n:
            A[i, i + 1] = 3
        if i - 1 >= 0:
            A[i, i - 1] = 1

    det_A = np.linalg.det(A)

    print("\nЗгенерована матриця:")
    print(A)
    print(f"\nВизначник матриці порядку {n} дорівнює: {det_A:.4f}")

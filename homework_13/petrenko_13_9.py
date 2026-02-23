def read_matrix_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.strip().split()]
            if row:
                matrix.append(row)

        if not matrix:
            return None
        size = len(matrix)
        for row in matrix:
            if len(row) != size:
                print(f"Помилка: матриця у файлі '{filename}' не квадратна або має невірний розмір.")
                return None
        return matrix
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None
    except ValueError:
        print(f"Помилка: файл '{filename}' містить нечислові дані.")
        return None


def multiply_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def compare_matrices(A, B):
    if len(A) != len(B) or len(A) != len(B):
        return False
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != B[i][j]:
                return False
    return True


def verify_product(m1, m2, m3, name1, name2, name3):
    product = multiply_matrices(m1, m2)
    if compare_matrices(product, m3):
        print(f"Твердження підтверджено: {name3} = {name1} * {name2}.")
        return True
    return False


file_a = "matrix_A.txt"
file_b = "matrix_B.txt"
file_c = "matrix_C.txt"

A = read_matrix_from_file(file_a)
B = read_matrix_from_file(file_b)
C = read_matrix_from_file(file_c)

if A is None or B is None or C is None:
    pass
else:
    found = False
    if verify_product(A, B, C, 'C', 'A', 'B'):  # Порядок аргументів змінено для коректного виводу назв
        found = True
    elif verify_product(B, A, C, 'C', 'B', 'A'):
        found = True
    elif verify_product(A, C, B, 'B', 'A', 'C'):
        found = True
    elif verify_product(C, A, B, 'B', 'C', 'A'):
        found = True
    elif verify_product(B, C, A, 'A', 'B', 'C'):
        found = True
    elif verify_product(C, B, A, 'A', 'C', 'B'):
        found = True

    if not found:
        print("Твердження спростовано: Жодна з матриць не є добутком двох інших.")

def mult(n, m):
    if n == 0:
        return 0
    return m + mult(n - 1, m)

if __name__ == '__main__':
     print(mult(3, 5))
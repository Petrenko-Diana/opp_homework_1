# if n = 0 -> 1
# n -> * f(n - 1)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    print(fact(5))
    print(fact(20))
# алгоритм евкліда
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

if __name__ == '__main__':
    a, b = [int(x) for x in input().split()]
    d = gcd(a, b)
    print(d)









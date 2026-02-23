def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_n(n):
    res = 1
    for i in range(2,n + 1):
        res = lcm(res, i)
    return res

if __name__ == '__main__':
    n = int(input())
    d = lcm_n(n)
    print(d)
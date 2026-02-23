def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a >= b:
        return gcd(a % b,b)
    if b >= a:
        return gcd(b % a, a)

if __name__ == '__main__':
    print(gcd(42, 24))
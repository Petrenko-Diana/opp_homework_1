import sys

def F(n: int) -> int:
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n % 10

def sumF(n: int) -> int:
    if n <= 0:
        return 0
    if n < 10:
        s = 0
        for i in range(1, n+1):
            s += F(i)
        return s

    k = n // 10
    r = n % 10
    res = sumF(k - 1) + 45 * k
    res += F(k)
    if r > 0:
        res += r * (r + 1) // 2

    return res

def S(p: int, q: int) -> int:
    if q < p:
        return 0
    return sumF(q) - sumF(p - 1)

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        p, q = map(int, parts[:2])
        if p < 0 and q < 0:
            break
        print(S(p, q))

if __name__ == "__main__":
    main()


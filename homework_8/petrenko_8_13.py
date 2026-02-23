import sys
import math

MOD = 10**8

def fib(n):
    if n == 0:
        return 0
    def fib_pair(n):
        if n == 0:
            return (0, 1)
        a, b = fib_pair(n >> 1)
        c = (a * ((b * 2 - a) % MOD)) % MOD
        d = (a * a + b * b) % MOD
        if n & 1:
            return (d, (c + d) % MOD)
        else:
            return (c, d)
    return fib_pair(n)[0]

def solve():
    for line in sys.stdin:
        n, m = map(int, line.split())
        g = math.gcd(n, m)
        print(fib(g) % MOD)

if __name__ == "__main__":
    solve()


def pairs_amount(A, B):
    if B % A != 0:
        return 0
    k = B // A
    if k == 1:
        return 1


    r = 0
    n = k
    d = 2
    while d * d <= n:
        if n % d == 0:
            r += 1
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        r += 1

    return 1 << r

if __name__ == "__main__":
    A, B = [int(x) for x in input().split()]
    print(pairs_amount(A, B))

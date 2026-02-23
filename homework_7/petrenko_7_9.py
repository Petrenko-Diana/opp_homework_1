def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def reverse_number(x):
    return int(str(x)[::-1])

def happy_prime(K):
    count = 0
    p = 2
    lim = 10**6

    while p <= lim:
        if is_prime(p):
            r = reverse_number(p)
            if r != p and is_prime(r):
                count += 1
                if count == K:
                    return p
        p += 1

    return -1
if __name__ == "__main__":
    K = int(input())
    print(happy_prime(K))

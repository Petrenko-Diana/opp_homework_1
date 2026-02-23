def pasc(n,k):
    if k == 0 or n == k:
        return 1
    return pasc(n-1,k-1) + pasc(n-1,k)
N = int(input())
for n in range(N):
    for k in range(n + 1):
        print(pasc(n, k), end=" ")
    print()



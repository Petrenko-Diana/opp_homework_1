n = int(input())

lst = [int(x) for x in input().split()]

for i in range(n):
    if lst[i] >= 0:
        lst[i] += 2
    print(lst[i], end=" ")

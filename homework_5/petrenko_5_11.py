n = int(input())
str = list(map(int, input().split()))
lst = [str[-1]] + str[:n-1]
print(*lst)
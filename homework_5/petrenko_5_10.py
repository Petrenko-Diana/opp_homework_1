n = int(input())
str = list(map(int, input().split()))
d = int(input())
lst = list(map(int, input().split()))

s = [x for x in str if x not in lst]
print(len(s))
print(*s)
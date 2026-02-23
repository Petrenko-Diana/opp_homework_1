n = int(input())
str = list(map(int, input().split()))
p = []
s = []
for x in str:
    if x not in p:
        p.append(x)
        s.append(x)
print(*s)

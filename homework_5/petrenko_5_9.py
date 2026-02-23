a, b, c, d = map(int, input().split())
p = set()
for i in range(min(a, b), max(a, b) + 1):
    for j in range(min(c, d), max(c, d) + 1):
        p.add(i * j)
print(len(p))
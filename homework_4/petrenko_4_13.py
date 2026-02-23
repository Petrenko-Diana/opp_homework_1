n = int(input())
s = 0
for x in range (10 , 100):
    a = x // 10
    b = x % 10
    d = n * x
    c = d // 100
    g = (d // 10) % 10
    f = d % 10
    if a + b == c + g +f:
        s += 1
print(s)
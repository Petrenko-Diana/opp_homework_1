n = int(input())

s = 0
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if n == 1:
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            s += x
    elif n == 2:
        if a < b < c:
            s += 1
    elif n == 3:
        if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
            s += x
    elif n == 4:
        if a > b > c:
            s += 1
    elif n == 5:
        if x == a ** 3 + b ** 3 + c ** 3:
            s += x
    elif n == 6:
        if a != b and a != c and c != b:
            s += 1
print(s)
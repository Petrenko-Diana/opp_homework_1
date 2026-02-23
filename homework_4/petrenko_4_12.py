s = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n % 2 == 0:
        s += n
print (s)
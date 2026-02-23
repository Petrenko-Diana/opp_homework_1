m = int(input())

def reverse_number(n):
    s = 0
    while n>0:
        s = s*10 + (n%10)
        n //= 10
    return s
t = m
h = 0

while True:
    s = reverse_number(t)
    if t == s:
        print(h)
        break
    else:
        t = t+s
        h = h+1
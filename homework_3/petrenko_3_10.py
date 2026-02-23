n = int(input())
s = 0
p = 1
while n>0:
    d = n%10
    if d%2==0:
        d = d + 1
    else:
        d = d - 1
    s += d*p
    p *= 10
    n = n//10
print(s)
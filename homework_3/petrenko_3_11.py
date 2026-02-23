n = int(input())
s = 0
f = False
while n>0:
    d = n%10
    if d%2==0:
        s += d
        f = True
    n = n//10
if f == True:
    print(s)
else:
    print("-1")
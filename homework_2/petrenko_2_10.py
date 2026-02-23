n = int(input())

d1 = n//100
d2 = n//10%10
d3 = n%10

if d1>d2 and d1>d3:
    print(d1)
elif d2>d1 and d2>d3:
    print(d2)
elif d1==d2 or d1==d3 or d2==d3:
    print("=")
else:
    print(d3)
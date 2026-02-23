import math
a, b, c = [int(n) for n in input().split()]


d = b**2 - 4*a*c
if d<0:
    print("No roots")
elif d == 0:
    x = -b / (2*a)
    print("One root: ", x)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    if x1>x2:
        print("Two roots:", x2, x1)
    else:
        print("Two roots:", x1, x2)
import math
x1, y1, r1, x2, y2 ,r2 = map(float, input().split())
d = math.hypot(x2-x1, y2-y1)

if d == 0 and r1 == r2:
    print ("-1")

elif d > r1 + r2 or d < abs(r1 - r2):
    print (0)

elif d == r1 + r2 or d == abs(r1 - r2):
    print ("1")

else:
    print ("2")

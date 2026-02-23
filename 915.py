a, b, c = [int(n) for n in input().split()]
if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
    print("YES")
else:
    print("NO")
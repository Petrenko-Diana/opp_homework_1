x, y, z = [int(n) for n in input().split()]
if x ==y and x==z:
    print("1")
elif x==y or x==z or y==z:
    print("2")
else:
    print("3")
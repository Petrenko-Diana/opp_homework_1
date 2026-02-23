x, y = [int(n) for n in input().split()]
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x==0 or y==0:
    print("0")
else:
    print("4")
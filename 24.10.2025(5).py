x, y, z = [float(n) for n in input().split()]
print(min(max(x,y), max(y,z), x + y + z))
import math
n = int(input())

f = 0
for i in range(1, n+1):
    f += math.log10(i)
print(int(f)+1)
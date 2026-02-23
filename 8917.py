
"""n = int(input())

i = 2
while i < n:
    print(i , end=" ")
    i *= 2"""

n = int(input())
i = 1

for s in range(1, n+1):
    i *= s
print(i)

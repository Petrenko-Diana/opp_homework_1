#n = int(input())


#for i in range(1, n + 1):
 #   print(i**2, end=" ")


a = 0
while True:
    n = int(input())
    if n == 0:
        break

    if n%2==0:
        continue
    else:
        a += 1
print(a)
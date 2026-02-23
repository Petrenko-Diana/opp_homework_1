# Умови if/elif/else
n = int(input("Введіть ціле число: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")
###################################
a, b = map(int, input().split())
if a > b:
    print(a)
elif b > a:
    print(b)
elif a == b:
    print("equal")
#######################################
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")

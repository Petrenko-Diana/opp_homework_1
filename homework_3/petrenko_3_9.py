n = int(input())

a = 1
while n > 0:
    if a%2!=0 and a%3!=0 and a%5!=0:
        print(a, end= " ")
        n = n - 1
    a = a + 1
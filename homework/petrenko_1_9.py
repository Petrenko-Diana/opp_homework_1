a, b, n = [int(n) for n in input().split()]
a_and_b = (a*100+b)*n
a1=a_and_b//100
b1=a_and_b%100

print(a1, b1)
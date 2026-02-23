import sys
sys.set_int_max_str_digits(56000)
m = int(input())

s = 1
f = 1
while f<m:
    s += 1
    f *= s
print(s)
# n = int(input())
#
# s = 0
# k = n
#
# while n>0:
#     d = n%10
#     n = n// 10
#     s = s * 10 + d
# if k == s:
#     print("YES")
# else:
#     print("NO")
##########################

n = int(input())

s = 0
p = 1

while n>0:
    d = n%10
    n = n// 10
    s = s + d*p
    p = p *2

print(s)
s = input()
p = ""
n = ''
for c in s:
    if p != c:
        n += c
        p =c

print(n)
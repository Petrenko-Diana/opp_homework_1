s = input()
counter = {}

max_c = ""
for c in s:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1
    if c > max_c:
        max_c = c
print(max_c, counter[max_c])
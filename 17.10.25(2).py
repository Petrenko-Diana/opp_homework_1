n = input()
count = 0
i = 0
while i < len(n):
    if n[1] in 'AYEIOU':
        count += 1
        i += 1
    else:
        i += 1
print(count)
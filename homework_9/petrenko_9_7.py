n = int(input())
s = input().strip()

counts = {}

for i in s:
    if i not in counts:
        counts[i] = 0
    counts[i] += 1

odd_letters = []

for i in counts:
    if counts[i] % 2 == 1:
        odd_letters.append(i)

if len(odd_letters) == 1:
    print(odd_letters[0])
else:
    print("Ok")

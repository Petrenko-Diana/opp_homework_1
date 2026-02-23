n = int(input())
lst = (float(x) for x in input().split())

count = 0
summ = 0

for i in range(n):
    if (i + 1) % 3 == 0 and lst[i] > 0:
        count += 1
        summ += lst[i]
print(count, f"{summ:.2f}")

n = int(input())
array = list(map(int, input().split()))

count = 0
prev_abs = None

for x in array:
    a = abs(x)

    # Якщо це нове абсолютне число
    if a != prev_abs:
        count += 1
        prev_abs = a

print(count)

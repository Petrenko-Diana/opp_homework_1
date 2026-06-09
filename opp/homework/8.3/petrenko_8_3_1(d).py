# Введення значення параметра n
n = int(input("Введіть ціле значення n (n >= 1): "))

if n < 1:
    print("Помилка! Значення n має бути більшим або рівним 1.")
else:
    a = [0, 0, 1]

    for k in range(3, n + 1):
        next_a = a[k - 1] + k * a[k - 2]
        a.append(next_a)

    S_n = 0
    for k in range(1, n + 1):
        S_n += (2 ** k) * a[k]

    print(f"Сума S_{n} дорівнює: {S_n}")

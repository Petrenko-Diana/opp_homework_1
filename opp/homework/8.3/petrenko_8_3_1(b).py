n = int(input("Введіть ціле значення n (n >= 1): "))

if n < 1:
    print("Значення n має бути більшим або рівним 1.")
else:
    P_n = 1.0
    for i in range(1, n + 1):
        term = 1 / (i + 1)
        P_n *= term

    print(f"Добуток P_n = {P_n}")

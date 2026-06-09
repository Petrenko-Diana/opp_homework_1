import math

x = float(input("Введіть значення x: "))
eps = float(input("Введіть точність: "))

if eps <= 0:
    print("Точність має бути більшою за 0.")
else:
    term = x
    taylor_sin = term
    i = 1

    while abs(term) > eps:
        term = term * (-x ** 2) / ((2 * i) * (2 * i + 1))
        taylor_sin += term
        i += 1

if __name__ == '__main__':
    math_sin = math.sin(x)
    difference = abs(taylor_sin - math_sin)

    print(f"\nРезультат через ряд Тейлора: {taylor_sin}")
    print(f"Результат через math.sin():   {math_sin}")
    print(f"Різниця між методами:        {difference}")
    print(f"Кількість врахованих членів:  {i}")

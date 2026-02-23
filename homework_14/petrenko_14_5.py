import math

def solve(a, b, c):
    assert a != 0, "Помилка: Коефіцієнт 'a' не може бути нулем. Це не квадратне рівняння."

    D = b ** 2 - 4 * a * c

    assert D >= 0, f"Помилка: Дискримінант від'ємний (D = {D}). Рівняння не має розв'язків на множині дійсних чисел."

    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    return x1, x2

print("x^2 - 3x + 2 = 0")
x1, x2 = solve(a=1, b=-3, c=2)
print(f"x1 = {x1}, x2 = {x2}\n")
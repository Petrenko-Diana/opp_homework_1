import math


def fibonacci_generating_function(x, eps):
    limit = (math.sqrt(5) - 1) / 2
    if not (0 < abs(x) < limit):
        raise ValueError(f"x має задовольняти умову 0 < |x| < {limit:.4f}")

    analytical_value = x / (1 - x - x ** 2)
    f0, f1 = 0, 1
    total_sum = f0 * (x ** 0)

    n = 1
    while True:
        term = f1 * (x ** n)
        total_sum += term

        f0, f1 = f1, f0 + f1
        n += 1

        if abs(term) < eps:
            break

    return total_sum, analytical_value


if __name__ == '__main__':
    x_val = 0.3
    eps_val = 1e-7
    series_res, exact_res = fibonacci_generating_function(x_val, eps_val)

    print(f"Результат суми ряду:  {series_res:.7f}")
    print(f"Аналітичне значення: {exact_res:.7f}")


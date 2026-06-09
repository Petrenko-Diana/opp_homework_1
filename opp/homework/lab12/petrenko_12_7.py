import math

def calc_shx(x, eps):
    term = x
    total_sum = term
    n = 1
    while True:
        term = term * (x ** 2) / ((2 * n) * (2 * n + 1))
        total_sum += term
        n += 1
        if abs(term) < eps:
            break
    return total_sum


def calc_ln(x, eps):
    term = x
    total_sum = term
    n = 1
    while True:
        n += 1
        term = ((-1) ** (n + 1)) * (x ** n) / n
        total_sum += term
        if abs(term) < eps:
            break
    return total_sum


def calc_inv_1x(x, eps):
    term = 1
    total_sum = term
    n = 1
    while True:
        term = ((-1) ** n) * (x ** n)
        total_sum += term
        n += 1
        if abs(term) < eps:
            break
    return total_sum


def calc_inv_1x_3(x, eps):
    term = 1
    total_sum = term
    n = 1
    while True:
        coeff = (n + 1) * (n + 2) // 2
        term = ((-1) ** n) * coeff * (x ** n)
        total_sum += term
        n += 1
        if abs(term) < eps:
            break
    return total_sum


def calc_sqrt_1x(x, eps):
    term = 1
    total_sum = term
    n = 1

    num = 1
    den = 2
    while True:
        term = ((-1)**(n-1)) * (num / den) * (x**n)
        total_sum += term
        num *= (2 * n - 1)
        den *= (2 * n + 2)
        n += 1
        if abs(term) < eps:
            break
    return total_sum


def calc_arcsinx(x, eps):
    term = x
    total_sum = term
    n = 1
    num = 1
    den = 2
    while True:
        term = (num / den) * (x ** (2 * n + 1)) / (2 * n + 1)
        total_sum += term
        num *= (2 * n - 1)
        den *= (2 * n + 2)
        n += 1
        if abs(term) < eps:
            break
    return total_sum

if __name__ == '__main__':
    eps = 1e-6
    x = 0.5

    print(f"a) sh({x}):\tРяд: {calc_shx(x, eps):.6f}\tMath: {math.sinh(x):.6f}")
    print(f"b) ln(1+{x}):\tРяд: {calc_ln(x, eps):.6f}\tMath: {math.log(1+x):.6f}")
    print(f"c) 1/(1+{x}):\tРяд: {calc_inv_1x(x, eps):.6f}\tMath: {1/(1+x):.6f}")
    print(f"d) 1/(1+{x})^3:\tРяд: {calc_inv_1x_3(x, eps):.6f}\tMath: {1/((1+x)**3):.6f}")
    print(f"e) sqrt(1+{x}):\tРяд: {calc_sqrt_1x(x, eps):.6f}\tMath: {math.sqrt(1+x):.6f}")
    print(f"f) arcsin({x}):\tРяд: {calc_arcsinx(x, eps):.6f}\tMath: {math.asin(x):.6f}")

def cubic_root_approx(x, eps, method='a'):
    if x <= 0:
        return "х має бути більшим за 0"

    x_prev = x / 3.0

    while True:
        x_next = (1 / 3) * (2 * x_prev + x / (x_prev ** 2))

        if method == 'a':
            if abs(x_next - x_prev) < eps:
                return x_next
        elif method == 'b':
            if abs(x_next ** 3 - x) < eps:
                return x_next

        x_prev = x_next


if __name__ == '__main__':
    x_input = 12.76
    eps_input = 1e-6

    res_a = cubic_root_approx(x_input, eps_input, method='a')
    res_b = cubic_root_approx(x_input, eps_input, method='b')
    exact = x_input ** (1 / 3)

    print(f"Кубічний корінь з {x_input}:")
    print(f"а):       {res_a:.6f}")
    print(f"б):       {res_b:.6f}")
    print(f"Точне значення:    {exact:.6f}")


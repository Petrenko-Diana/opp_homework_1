def max_fibonacci_less_than_a(a):
    if a < 0:
        return "Число Фібоначчі не існує для від'ємних значень"

    f0 = 0
    f1 = 1
    if a == 0:
        return 0

    while f1 <= a:
        f0, f1 = f1, f0 + f1

    return f0

if __name__ == '__main__':
    a = 50
    print(f"Найбільше число Фібоначчі <= {a}: {max_fibonacci_less_than_a(a)}")

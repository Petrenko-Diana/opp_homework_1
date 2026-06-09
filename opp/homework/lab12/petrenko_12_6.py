def find_max_sequence_member(a):
    x0 = 1
    x1 = 0
    x2 = 1

    initials = [x0, x1, x2]
    valid = [x for x in initials if x <= a]

    if not valid and a < min(initials):
        return "Немає членів послідовності, які не перевищують a"

    prev3 = x0
    prev2 = x1
    prev1 = x2
    max_val = max(valid) if valid else x0
    max_idx = initials.index(max_val)

    n = 3
    while True:
        xn = 2 * prev1 + 3 * prev3
        if xn > a:
            break

        max_val = xn
        max_idx = n

        prev3 = prev2
        prev2 = prev1
        prev1 = xn
        n += 1

    return max_val, max_idx


if __name__ == '__main__':
    a = 100
    val, idx = find_max_sequence_member(a)
    print(f"Для a={a}: найбільший член x_{idx} = {val}")


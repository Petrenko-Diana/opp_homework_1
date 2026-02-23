def unique_digits(n):
    s = str(n)
    return len(set(s)) == 4


def main():
    a, b = map(int, input().split())

    result = []
    for n in range(a, b + 1):
        if unique_digits(n):
            result.append(str(n))

    print(" ".join(result))

if __name__ == "__main__":
    main()

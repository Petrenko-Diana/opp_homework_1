digits = "0123456789abcdefghijklmnopqrstuvwxyz"

def to_base(n, b):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        s = digits[n % b] + s
        n //= b
    return s

def is_pal(s):
    return s == s[::-1]

def main():
    n = int(input())

    good = []
    for b in range(2, 37):
        if is_pal(to_base(n, b)):
            good.append(b)

    if not good:
        print("none")
    elif len(good) == 1:
        print("unique")
    else:
        print("multiple")

    if good:
        print(good)
if __name__ == "__main__":
    main()
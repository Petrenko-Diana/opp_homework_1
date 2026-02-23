def to_base13(n: int) -> str:
    symbols = "0123456789ABC"
    if n < 13:
        return symbols[n]
    return to_base13(n // 13) + symbols[n % 13]

if __name__ == "__main__":
    n = int(input())
    print(to_base13(n))

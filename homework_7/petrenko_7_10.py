digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(num_str, base):
    value = 0
    for ch in num_str:
        d = digits.index(ch)
        value = value * base + d
    return value

def from_decimal(value, base):
    if value == 0:
        return "0"
    res = []
    while value > 0:
        res.append(digits[value % base])
        value //= base
    return "".join(reversed(res))

if __name__ == "__main__":
    m, k = map(int, input().split())
    num_str = input().strip()
    value = to_decimal(num_str, m)
    result = from_decimal(value, k)
    print(result)
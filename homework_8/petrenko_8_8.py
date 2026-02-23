def square(n: int) -> str:
    b = bin(n)[2:]
    lst = []
    for ch in b:
        if ch == '1':
            lst.append('SX')
        else:
            lst.append('S')
    s = ''.join(lst)
    return s[2:] if len(s) >= 2 else ''

if __name__ == "__main__":
    n = int(input())
    print(square(n))

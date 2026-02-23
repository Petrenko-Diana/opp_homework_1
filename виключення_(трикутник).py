def square(a, b, c):
    assert a + b > c and a + c > b and b + c > a, "the triangle doesn't exist"

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

if __name__ == '__main__':
    a, b, c = [int(x) for x in input().split()]
    print(square(a, b, c))
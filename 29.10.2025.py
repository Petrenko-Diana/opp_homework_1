

def full_squares(lst):
    res = []
    for x in lst:
        sqrt = x**0.5
        if sqrt == int(sqrt):
            res.append(x)
    return res

def powers_of_five(lst):
    res = []
    for x in lst:
        y = x
        while y % 5 == 0:
            y = y // 5
        if y == 1:
            res.append(x)
    return res
def is_prime(lst):
    res = []
    for x in lst:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                break
        else:
                res.append(x)
    return res

def main():
    lst = [5, 654, 23, 49, 865, 7765, 43, 71, 64, 50, 33, 125]
    print(full_squares(lst))
    print(powers_of_five(lst))
    print(is_prime(lst))

if __name__ == '__main__':
    main()
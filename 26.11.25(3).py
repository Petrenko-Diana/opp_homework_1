def read_numbers(filename):
    f = open(filename)
    numbers = []
    for line in f:
        numbers = [float(x) for x in f.readline().split()]
    f.close()
    return numbers

def a(filename):
    numbers = read_numbers(filename)
    return sum(numbers)

filename = "matrix.txt"
print(a(filename))

def b(filename, sixe = 60):
    """в) виведення рядків які містять більше 60"""
    with open("input.txt") as f:
        for line in f:
            if len(line) > size:
                print(len(line), line, end="")

def c(filename):
    count = 0
    f = open(filename)
    while True:
        line = f.readline()
        if line == "\n":
            count += 1
        print(line, end="")
        if line == "":
            break
    f.close()

    def d(filename):
        max_line = ""
        max_size = 0
        f = open(filename)
        for line in f:
            if len(line) > max_size:
                max_size = len(line)
                max_line = line
        f.close()
        print(max_line)
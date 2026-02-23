with open("input.txt") as f:
    words = []
    for line in f:
        words += line.split()
    print(words)
for word in words:
    print(len(word), end = " ")
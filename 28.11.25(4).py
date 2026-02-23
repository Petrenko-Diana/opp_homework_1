wallet = {1: 3, 2: 2, 3: 5, 10: 24, 25: 1, 50: 5}

s = 0
for i in range(101):
    try:
        s += wallet[i] * i
    except KeyError:
        continue
print(s)

text = "Hello World"
index =
















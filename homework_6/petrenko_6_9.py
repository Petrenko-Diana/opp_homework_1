str = input()

count = 0
for i in str:
    if i in "+*-**/%":
        count += 1

print(count)
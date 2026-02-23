

n = input()
result = ""
for char in n:
    result += char
    if char in "aeiuyo":
        result += char
print(result)
str = input()

result = ""
for i in str:
    result += i
    if i.islower():
        result += i
print(result)
code = input()
s = int(input())

str = ""
for i in code:
    n = chr((ord(i) - ord('A') - s) % 26 + ord('A'))
    str += n
print(str)

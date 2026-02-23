str = input()

s = str.replace(" ","")
if s == s[::-1]:
    print("YES")
else:
    print("NO")

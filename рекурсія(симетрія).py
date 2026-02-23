def is_symmetric(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_symmetric(s[1:-1])

print(is_symmetric("adda"))
print(is_symmetric("riheiotyu"))


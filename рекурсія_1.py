# def invert(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return s[-1] + invert(s[:-1])
#
# print(invert("sparire"))

# def replace(s, c, repl):
#     if s == "":
#         return ""
#     elif c == s[0]:
#         return repl + replace(s[1:], c, repl)
#     else:
#         return s[0] + replace(s[1:], c, repl)
# print(replace("circle", "c", "1"))













def replace(s, c, repl):
    if s == "":
        return s
    elif s[0] == c:
        return repl + replace(s[1:], c, repl)
    else:
        return s[0] + replace(s[1:], c, repl)
print(replace('ovulation', 'l', 'll'))
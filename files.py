# f = open("input_txt", "a")
# print("World", file=f)
# f.close()
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])


# def func(s):
#     if s != 0:
#         return max(func(s // 10), s % 10)
#     else:
#         return 0

def foo(bar):
    if len(bar) == 0:
        return ""
    else:
        return foo(bar[1:]) + bar[0]
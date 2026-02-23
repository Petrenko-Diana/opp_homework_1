# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
# print(is_prime(7)
#
########################## Приймає список чисел, повертає кортеж з трьох елементів: мінімум, максимум, сер.ар
lst = [3, 7, 1, 9, 4]
def status(lst):
    maximum = lst[0]
    minimum = lst[0]
    total = 0
    for i in lst:
        total += i
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i
    return maximum, minimum, total/len(lst)
print(status(lst))
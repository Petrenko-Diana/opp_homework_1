# Створити слонвик, порахувати середній бал
# n = int(input())
# dictionary = {}
#
# total = 0
# for i in range(n):
#     name = input()
#     points = int(input())
#     dictionary[name] = points
#
# for points in dictionary.values():
#     total += points
# average = total / len(dictionary)
# print(dictionary)
# print(average)

####################################### daddy made me fight  |   d : 4, a : 2
# string = "daddy made me fight, it wasn't always right, but he said girl it's your second amendment"
# dicti = {}
#
# for ch in string:
#     if ch not in dicti:
#         dicti[ch] = 1
#     elif ch in dicti:
#         dicti[ch] += 1
# print(dicti)

######################## Дано список слів. Створити словник. Ключ - довжина слова, значення - список слів такої довжини
lst = ['day', 'after', 'day']
groups = {}
for elem in lst:
    length = len(elem)
    if length in groups:
        groups[length].append(elem)
    else: groups[length] = [elem]
print(groups)
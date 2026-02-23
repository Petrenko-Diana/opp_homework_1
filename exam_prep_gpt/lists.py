n = int(input())
num = []
for i in range(n):
    x = int(input())
    num.append(x)

max = num[0]
min = num[0]
summ = 0

for i in num:
    summ += i
    if i > max:
        max = i
    if i < min:
        min = i
print(max, min, summ)

###########################Новий список лише з парними
lst = [2, 11, 34, 67, 56, 80,3, 5]
lst_even = []
for i in lst:
    if i % 2 == 0:
        lst_even.append(i)
print(lst_even)
################################## Другий найбільший
num = [1, 5, 65, 43, 33, 9, 0, 65, 49]

if num[0] > num[1]:
    max1 = num[0]
    max2 = num[1]
else:
    max1 = num[1]
    max2 = num[0]

for i in num[2:]:
    if i > max1:
        max1 = i
        max2 = max1
    elif i > max2 and i != max1:
        max2 = i
print(max2)

################################## Видалити дублікати, залишивши лише унікальні

lst = [2, 33, 4, 43, 33, 5, 43, 8, 4]
lst_set = []
for i in lst:
    if i not in lst_set:
        lst_set.append(i)
print(lst_set)



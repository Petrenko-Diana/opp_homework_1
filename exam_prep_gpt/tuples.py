num = (0, 5, -6, 8, -3, 1, 2) # кортеж
pos = 0  # count of positive
neg = 0  #count of negative
for i in num:
    if i == 0:
        pass
    elif i > 0:
        pos += 1
    else:
        neg += 1
print(pos, neg)

########################## Перетворити кортеж у список, поміняти місцями перший і останній елементи, повернути назад у кортеж

t = (1, 2, 3, 4, 5, 6)
lst = list(t)
if len(lst) > 1:
    lst[0], lst[-1] = lst[-1], lst[0]
t = tuple(lst)
print(t)
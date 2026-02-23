a = input()
b = input()

counter1 = {}
for i in a:

    if i in counter1:
        counter1[i] += 1 #index
        counter1[i] = 1 #count
    else:
        counter1[i] = 1#index, item, count

counter2 = {}
for i in b:

    if i in counter2:
        counter2[i] += 1 #index
        counter2[i] = 1 #count
    else:
        counter2[i] = 1

for x in b:
    if x not in counter1:
        print("NO")
    elif counter1[x] < counter2[x]:
        print("NO")
        break
    else:
        print("OK")

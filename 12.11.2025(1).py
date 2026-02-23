N = int(input())
array = [int(x) for x in input().split()]

count = {}
for x in array:
    if x in count:
        count[x] = count[x] + 1
    else:
        count[x] = 1

for key, value in count.items():
    if value == 1:
        print(key, end=" ")


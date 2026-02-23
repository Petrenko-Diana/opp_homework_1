#Цикли for, while
n = int(input())
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s += i
print(s, end="  ")

##########################
s = 0
while n != 0:
    n = int(input())
    s += n
print(s)

#################
k = int(input())
for i in range(1, 11):
    m = k * i
    print(k, "*", i, "=", m)

###########################
n = int(input())
count = 0
if n == 0:
    count = 1
while n > 0:
    n = n // 10
    count += 1
print(count)
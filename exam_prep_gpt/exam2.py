# count=0
# for n in range(1001,100000):
#     s=str(n)
#     if s==s[::-1] and '8'in s:
#         count +=1
# print(count)

def palindrom(m):
    str_m = str(m)
    if str_m == str_m[::-1] and '8'in str_m:
        return True
    else:
        return False

counter = 0
for m in range(10000,100001):
    if palindrom(m) == True:
        counter += 1
    else:
        counter += 0
print(counter)

def palindrom(m):
    str_m = str(m)

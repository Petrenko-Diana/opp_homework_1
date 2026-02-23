n = int(input())
str = list(map(float, input().split()))
s = [x for x in str if x > 0]
if len(s) == 0:
    print("Not Found")
else:
    summ = sum(s)/len(s)
    print(f"{summ:.2f}")
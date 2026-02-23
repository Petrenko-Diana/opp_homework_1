str = input()
count = 0
if any(i.islower() for i in str):
    count += 1
if any(i.isupper() for i in str):
    count += 1
if any(i.isdigit() for i in str):
    count += 1
if any(i in ['!','"','#','$','%','&',"'",'(',')','*','+'] for i in str):
    count += 1
if len(str) >= 8:
    count += 1
print(count)
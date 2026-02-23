s = "5fccb4 23 lgfc 4 sfc 89 \' 34 \"\"\",, ,,,, 45 21 yr4 a 4e 29"

summ = 0
for c in s:
    try:
        summ += int(c)
    except ValueError:
        pass
print(summ)
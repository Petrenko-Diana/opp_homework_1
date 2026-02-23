n = int(input())

main_sum = 0
secondary_sum = 0

for i in range(n):
    row = list(map(int, input().split()))
    main_sum += row[i]
    secondary_sum += row[n-1-i]

print(main_sum, secondary_sum)

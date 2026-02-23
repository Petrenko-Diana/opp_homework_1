n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

r, c = map(int, input().split())

for i in range(r):
    print(*matrix[i][:c])
x = int(input())
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for c in range(n):
    g = False
    for row in range(n):
        if matrix[row][c] == x:
            g = True
            break
    print("YES" if g else "NO")
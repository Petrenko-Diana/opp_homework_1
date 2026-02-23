t = int(input())  # кількість тестів

for _ in range(t):
    V = int(input())
    votes = [int(input()) for _ in range(V)]

    count = {}
    for num in votes:
        if num not in count:
            count[num] = 0
        count[num] += 1

    max_votes = max(count.values())

    candidates = [num for num, c in count.items() if c == max_votes]

    print(min(candidates))

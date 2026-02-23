def gen_perm(curr_perm, used, n):
    if len(curr_perm) == n:
        print(*curr_perm)
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            curr_perm.append(i)

            gen_perm(curr_perm, used, n)

            curr_perm.pop()
            used[i] = False

if __name__ == "__main__":
    n = int(input())
    used = [False] * (n + 1)
    gen_perm([], used, n)

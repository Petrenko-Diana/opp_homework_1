import sys

def solve():
    case_no = 1
    for line in sys.stdin:
        k, n, t = map(int, line.split())
        if k == 0 and n == 0 and t == 0:
            break

        m = 10 ** t
        result = pow(k, n, m)  # швидке піднесення до степеня під модулем
        print(f"Case #{case_no}: {result}")
        case_no += 1

if __name__ == "__main__":
    solve()



def is_ok(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if is_ok(x):
                n_queen(x + 1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    ans = 0
    row = [0] * n
    n_queen(0)

    print("#{} {}".format(tc, ans))

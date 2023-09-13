T = int(input())

for tc in range(1, T+1):
    size = int(input())
    ans = input()
    wrote = input()
    result = 0

    for i in range(size):
        if ans[i] == wrote[i]:
            result += 1

    print("#{} {}".format(tc, result))
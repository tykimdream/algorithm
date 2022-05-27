T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    time = [0] * 11112

    que = list(map(int, input().split()))

    count = 0
    fish = 0
    j = 0
    result = "Possible"
    for i in range(max(que)):
        if count == m:
            count = 0
            fish += k
        if i == que[j]:
            j += 1
            if fish > 0:
                fish -= 1
            else:
                result = "Impossible"
                break
        count += 1

    print("#{} {}".format(tc, result))
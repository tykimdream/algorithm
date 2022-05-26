T = int(input())

for tc in range(1, T+1):
    l, u, x = map(int, input().split())
    if x > u:
        result = -1
    elif x < l:
        result = l - x
    else:
        result = 0
    print("#{} {}".format(tc, result))
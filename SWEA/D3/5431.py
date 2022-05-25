T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [0] * (n + 1)
    arr[0] = 1
    submit = list(map(int, input().split()))

    for i in range(k):
        arr[submit[i]] += 1

    print("#{}".format(tc), end=' ')
    for i in range(n+1):
        if arr[i] == 0:
            print(i, end=' ')
    print()
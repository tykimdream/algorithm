T = int(input())

for tc in range(1, T+1):
    case = int(input())
    grade = list(map(int, input().split()))
    arr = [0] * 101
    for i in grade:
        arr[i] += 1
    mx = 0
    for i in range(101):
        if arr[mx] <= arr[i]:
            mx = i

    print("#{} {}".format(tc, mx))
    # print(target)
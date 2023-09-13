T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    # a에 짧은 배열을 저장
    # b에 긴 배열을 저장
    if n > m:
        a = arr2
        b = arr1
        gap = n - m + 1
        dis = m
    else:
        a = arr1
        b = arr2
        gap = m - n + 1
        dis = n

    for i in range(gap):
        local_sum = 0
        for j in range(dis):
            local_sum += (a[j] * b[i + j])
        if i == 0:
            temp = local_sum
        if temp < local_sum:
            temp = local_sum
    print("#{} {}".format(tc, temp))
T = int(input())

for tc in range(1, T+1):
    size = int(input())
    result = -1
    arr = list(map(int, input().split()))
    for i in range(size):
        for j in range(i+1, size):
            # print("i j i * j", i, j, arr[i] * arr[j])
            t = arr[i] * arr[j]
            if t < 10:
                result = max(t, result)
            else:
                if t > result:
                    temp = "".join(sorted(str(t)))
                    if int(temp) == t:
                        result = max(t, result)
    print("#{} {}".format(tc, result))

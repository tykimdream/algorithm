T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    target = sum(arr) // n
    result = 0

    for x in arr:
        if x > target:
            result += x - target
    print("#{} {}".format(tc, result))
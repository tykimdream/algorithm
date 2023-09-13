T = int(input())

for tc in range(1, T+1):
    size = int(input())
    word = list(map(str, input().split()))

    cut = len(word) // 2
    if size % 2 == 1:
        cut += 1
    arr1 = word[0:cut]
    arr2 = word[cut:]

    result = []
    for i in range(size):
        if i % 2 == 0:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    print("#{}".format(tc), *result)

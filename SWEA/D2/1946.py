T = int(input())

for tc in range(1, T+1):
    var = int(input())
    arr = []
    for _ in range(var):
        char, count = input().split()
        count = int(count)
        for _ in range(count):
            arr.append(char)
    print("#{}".format(tc))
    len_count = 1
    for i in arr:
        print(i, end='')
        len_count += 1
        if len_count == 10:
            print()
            len_count = 0
    print()
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    print("#{}".format(tc), end=' ')
    for i in range(n):
        print("{}/{}".format(1, n), end=' ')
    print()
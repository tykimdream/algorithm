T = int(input())

for tc in range(1, T+1):
    stu = list(map(int, input().split()))

    wrack = 0
    for i in stu:
        if i < 40:
            wrack += 40 - i
    result = sum(stu) + wrack
    print("#{} {}".format(tc, int(result / 5)))
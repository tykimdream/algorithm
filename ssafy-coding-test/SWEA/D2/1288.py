T = int(input())

for tc in range(1, T + 1):
    sheep = int(input())
    dic = [0] * 10
    result = 0

    while 0 in dic:
        result += 1
        xn = str(sheep * result)
        # print(result, dic)
        for i in range(len(xn)):
            dic[int(xn[i])] += 1

    print("#{} {}".format(tc, xn))

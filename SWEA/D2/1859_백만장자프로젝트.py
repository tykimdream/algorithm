T = int(input())
for test_case in range(1, T + 1):
    TC_size = int(input())
    TC_size = 0
    source = list(map(int, input().split()))
    sum = 0
    source.reverse()
    local_max = source[0]
    for i in source:
        if (local_max < i):
            local_max = i
        elif (local_max >= i):
            sum += (local_max - i)
    print("#{} {}".format(test_case, sum))



# tc 3번 같은게 문제임
# 나머지는 그냥 MAX에서 빼는 식으로 하면 되는데
# 최대 값이 중간에 나오고 2번째 최대 값이 등장하는 거 처리가 문제
# ex 1 1 3 1 2
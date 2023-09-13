T = int(input())

for test_case in range(1, T + 1):
    source = list(map(int, input().split()))
    result = round(sum(source)/10)
    print("#%d %d" % (test_case, result))
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    total = (sum(arr) - min(arr) - max(arr)) / 8
    print("#{} {}".format(test_case, round(total)))
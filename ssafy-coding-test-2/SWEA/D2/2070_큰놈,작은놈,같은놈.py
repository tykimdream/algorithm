T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    op = 'a'
    if (a > b):
        op = ">"
    elif (a < b):
        op = "<"
    elif (a == b):
        op = "="
    print("#{} {}".format(test_case, op))
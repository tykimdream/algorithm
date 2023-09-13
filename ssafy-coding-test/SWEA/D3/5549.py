T = int(input())

for tc in range(1, T+1):
    case = int(input())
    result = "Even"
    if case % 2 == 1:
        result = "Odd"
    print("#{} {}".format(tc, result))
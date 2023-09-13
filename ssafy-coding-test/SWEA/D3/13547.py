T = int(input())

for tc in range(1, T+1):
    stat = input()
    win_count = stat.count('o')
    result = "YES"
    if len(stat) == 15:
        if win_count >= 8:
            result = "YES"
        else:
            result = "NO"
    else:
        if stat.count('x') >= 8:
            result = "NO"
        if 15 - len(stat) + win_count >= 8:
            result = "YES"
        else:
            result = "NO"

    print("#{} {}".format(tc, result))
    #
    # rest = 15 - len(stat)
    # if win_count + rest >= 8:
    #     result = "YES"
    #     print("#{} {}".format(tc, result))
    # else:
    #     result = "NO"
    #     print("#{} {}".format(tc, result))

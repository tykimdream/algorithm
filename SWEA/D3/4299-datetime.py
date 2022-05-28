from datetime import datetime

T = int(input())
that_day = datetime(2022, 11, 11, 11, 11)
for tc in range(1, T+1):
    d, h, m = map(int, input().split())
    this_day = datetime(2022, 11, d, h, m)

    diff = (this_day - that_day)
    if that_day > this_day:
        result = -1
    else:
        result = round(diff.seconds / 60 + (diff.days * 1440))
    print("#{} {}".format(tc, result))

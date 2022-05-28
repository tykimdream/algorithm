from datetime import datetime

T = int(input())

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    time1 = datetime(2021, m1, d1)
    time2 = datetime(2021, m2, d2)
    print("#{} {}".format(tc, (time2 - time1).days + 1))

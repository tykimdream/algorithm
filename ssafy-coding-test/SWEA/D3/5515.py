from datetime import date

T = int(input())

for tc in range(1, T+1):
    m, d = map(int, input().split())
    day = date(2016, m, d)
    print("#{} {}".format(tc, day.weekday()))
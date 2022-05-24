import math
T = int(input())

for tc in range(1, T+1):
    n, d = map(int, input().split())
    restul = math.ceil(n / ((d * 2) + 1))
    print("#{} {}".format(tc, restul))

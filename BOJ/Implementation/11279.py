import heapq
import sys

n = int(input())
hip = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(hip, (-x, x))
    else:
        if hip:
            print(hip[0][1])
            heapq.heappop(hip)
        else:
            print(x)
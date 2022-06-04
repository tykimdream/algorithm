import heapq
import sys
n = int(input())
hip = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if hip:
            print(heapq.heappop(hip))
        else:
            print(x)
    else:
        heapq.heappush(hip, x)

# 7번 라인에서 input에서 시간 초과뜸
# 마지막에 int 안달아줌
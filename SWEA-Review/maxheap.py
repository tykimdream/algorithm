import heapq
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    heap = []
    printing = []
    for _ in range(n):
        op = list(map(int, input().split()))
        if op[0] == 1:
            heapq.heappush(heap, (-op[1], op[1]))
        if op[0] == 2:
            if heap:
                temp = heapq.heappop(heap)
                printing.append(temp[1])
            else:
                printing.append(-1)
    print("#{}".format(tc), end=' ')
    print(*printing)
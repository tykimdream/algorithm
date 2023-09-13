import heapq

T = int(input())

for tc in range(1, T+1):
    order = int(input())
    heap = []

    print("#{}".format(tc), end=' ')
    print_value = []
    for _ in range(order):
        op = list(map(int, input().split()))
        if op[0] == 1:
            heapq.heappush(heap, (-op[1], op[1]))
        elif op[0] == 2:
            if heap:
                print_value.append(heapq.heappop(heap)[1])
            else:
                print_value.append(-1)
    print(*print_value)
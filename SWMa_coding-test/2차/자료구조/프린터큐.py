# 1966
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    printer = list(map(int, input().split()))
    idx = list(range(len(printer)))
    idx[m] = 'target'

    order = 0

    while True:
        if printer[0] == max(printer):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                printer.pop(0)
                idx.pop(0)
        else:
            idx.append(idx.pop(0))
            printer.append(printer.pop(0))

N = int(input())
for test_case in range(1, N+1):
    limit = int(input())
    total = 0
    for i in range(1, limit+1):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    print("#{} {}".format(test_case, total))

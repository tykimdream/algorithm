T = int(input())
for test_case in range(1, T + 1):
    source = list(map(int, input().split()))
    result = 0
    for x in source:
       if x % 2 == 1:
         result+=x
    print("#{} {}".format(test_case, result))
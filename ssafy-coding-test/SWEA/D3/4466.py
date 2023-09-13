T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    total = sum(arr[0:k])
    print("#{} {}".format(tc, total))
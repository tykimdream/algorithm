# https://www.acmicpc.net/problem/2512

n = int(input())
region = list(map(int, input().split()))
country = int(input())

start = 1
end = max(region)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in region:
        if i > mid:
            sum += mid
        else:
            sum += i
    if sum <= country:
        start = mid+1
    else:
        end = mid-1
print(end)

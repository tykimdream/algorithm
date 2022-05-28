n, m = map(int, input().split())
wood = list(map(int, input().split()))

start = 1
end = max(wood)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in wood:
        if i >= mid:
            total += i - mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
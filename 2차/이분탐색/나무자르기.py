# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
wood = list(map(int, input().split()))

start = 1
end = max(wood)

# 시간 초과
# while start <= end:
#     sum = 0
#     mid = (start+end) // 2
#     for tree in wood:
#         if tree - mid > 0:
#             sum += tree - mid
#     if sum < m:
#         end = mid-1
#     else:
#         start = mid + 1

while start <= end:
    sum = 0
    mid = (start+end) // 2
    for tree in wood:
        if tree >= mid:
            sum += tree - mid
    if sum >= m:
        start = mid + 1
    else:
        end = mid-1

print(end)

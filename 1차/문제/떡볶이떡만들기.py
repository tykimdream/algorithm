# My sol
# n, m = map(int, input().split())

# dok = list(map(int, input().split()))

# ruler = max(dok)
# sum = 0
# while True:
#     for i in range(n):
#         if dok[i] > ruler:
#             dok[i] -= 1
#             sum += 1
#     if sum >= m:
#         break
#     else:
#         ruler -= 1

# print(sum)
# print(ruler)

# 파라메트릭 서치 (이진탐색 활용)
n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:  # 필요한 떡보다 적게 짤린 경우
        end = mid - 1
    else:  # 충분한 떡을 자른 경우
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)

# n: 떡의 개수, m: 요청한 떡의 길이
# 이때 최소 m을 만드는 절단기에 최대 높이를 구하라
n, m = 4, 6
arr = [19, 15, 10, 17]

start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    # 현재 길이에서 잘랐을 때 떡의 합
    for i in arr:
        if i > mid:
            sum += i - mid
    if sum < m:
        end = mid-1
    else:
        start = mid + 1
        result = mid
    # result = max(result, mid)

print(result)

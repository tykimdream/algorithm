from collections import Counter
T = int(input())

arr = []
for _ in range(T):
    arr.append(int(input()))

# 산술평균
print(round(sum(arr) / len(arr)))

# 중앙값
arr.sort()
print(arr[len(arr)//2])

# 최빈값
cnt = Counter(arr)
mode = cnt.most_common(1)
print(mode[0][0])

# 범위
print(arr[-1] - arr[0])
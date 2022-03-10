# 1920
from bisect import bisect_left, bisect_right
n = int(input())

dic = list(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

# 시간초과
# for i in find:
#     count = 0
#     for j in dic:
#         if j == i:
#             count += 1
#     print(count)

# 정렬하고 바이섹으로 구해보자


def range_value(graph, value):
    lft_idx = bisect_left(graph, value)
    rgt_idx = bisect_right(graph, value)
    return rgt_idx-lft_idx


dic.sort()

for i in find:
    if range_value(dic, i) == 0:
        print(0)
    else:
        print(1)

# 있으면 1, 없으면 0인데 그냥 갯수로 return해서 한번 더 틀렸음

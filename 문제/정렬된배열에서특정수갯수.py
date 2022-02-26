# n, x = map(int, input().split())
# target = list(map(int, input().split()))

# count = 0
# for i in range(n):
#     if target[i] == x:
#         count += 1

# print(count)

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
target = list(map(int, input().split()))
count = 0


def range_gap(arr, left, right):
    left = bisect_left(arr, left)
    right = bisect_right(arr, right)
    return right - left


print(range_gap(target, x, x))

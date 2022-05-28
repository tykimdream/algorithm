from bisect import bisect_left, bisect_right


def if_in(arr, i):
    left_idx = bisect_left(arr, i)
    right_idx = bisect_right(arr, i)
    return right_idx - left_idx


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
for i in arr2:
    if if_in(arr1, i) > 0:
        print(1)
    else:
        print(0)

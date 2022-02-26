# 파이썬 이진탐색 라이브러리
from bisect import bisect, bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))
# 정렬된 순서를 유지하면 배열 a에 x를 삽입할 가장 왼쪽(오른쪽)인덱스 반환


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if arr[mid] == target:
        return mid+1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print('원소를 찾을 수 없습니다.')
else:
    print(result, "번째에 위치합니다.")


def bin(arr, target, start, end):  # re
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == target:
        return mid+1
    elif arr[mid] > target:
        return bin(arr, target, start, mid-1)
    else:
        return bin(arr, target, mid+1, end)


result = bin(arr, target, 0, n-1)
print(result)

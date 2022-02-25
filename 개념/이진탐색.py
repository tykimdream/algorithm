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

# re


def bin(arr, target, start, end):
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

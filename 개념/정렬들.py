# 선택정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    for j in range(i, 0, -1):   # 인덱스 i부터 1까지 1씩 감소하며
        if arr[j] < arr[j-1]:  # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(arr)

# 퀵 정렬 (피벗 정렬) {표준 라이브러리에서 제공하는 정렬}
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 오른쪽에서 각각 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)


# 퀵정렬 2 파이썬의 맛
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있을 경우 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 피벗은 첫 원소
    tail = arr[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 오른쪽에서 각각 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(arr))

# 계수 정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작
# 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr = [5, 7, 9, 0, 3, 1, 6, 4, 8]

count = [0] * (max(arr) + 1)
print("max +1 : ", (max(arr)+1), "len(arr) : ", len(arr))
# count = [0] * len(arr)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

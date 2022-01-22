############ 2751 수 정렬하기2 ############
# N = int(input())
# arr = [int(input()) for i in range(N)]

## 오답 1 시간 초과 ##
# arr.sort()

# for i in arr:
#     print(i)

## sol 1 merge_sort ##

# def merge_sort(array):
#     if(len(array) <= 1):
#         return array
#     mid = len(array) // 2
#     left = merge_sort(array[: mid])
#     right = merge_sort(array[mid:])

#     i, j, k = 0, 0, 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             array[k] = left[i]
#             i += 1
#         else:
#             array[k] = right[j]
#             j += 1
#         k += 1

#     if i == len(left):
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#     elif j == len(right):
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#     return array

# arr = merge_sort(arr)

# for i in arr:
#     print(i)

## sol 2 pypy3 sorted ##
# N = int(input())
# arr = [int(input()) for i in range(N)]

# for i in sorted(arr):
#     print(i)

## sol 3 pypy3 sort ##
# N = int(input())
# arr = [int(input()) for i in range(N)]
# arr.sort()

# for i in arr:
#     print(i)


############ 11650 좌표 정렬하기 ############
# n = int(input())

# corrd = []

# for i in range(n):
#     [a, b] = map(int, input().split())
#     corrd.append([a, b])

# ans = sorted(corrd)
# for i in range(n):
#     print(ans[i][0], ans[i][1])

############ 11651 좌표 정렬하기2 ############
# n = int(input())

# corrd = []

# for i in range(n):
#     [b, a] = map(int, input().split())
#     corrd.append([a, b])

# ans = sorted(corrd)

# for i in range(n):
#     print(ans[i][1], ans[i][0])

############# 10814 나이순 정렬 ############
n = int(input())

person = []

for i in range(n):
    [old, name] = (input().split())
    person.append([old, name])

ans = sorted(person)

for i in range(n):
    print(ans[i][0], ans[i][1])


############# 10825 국영수 ############
############# 10989 수 정렬하기3 ############
############# 11652 카드 ############
############# 11004 K번째 수 ############

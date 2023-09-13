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
# n = int(input())

# person = []

# for i in range(n):
#     age, name = map(str, input().split())
#     age = int(age)
#     person.append((age, name))

# person.sort(key=lambda x: x[0])

# for i in person:
#     print(i[0], i[1])


############# 10825 국영수 ############
# 틀림, 정렬 순서가 다름
# n = int(input())
# list = []

# for _ in range(n):
#     name, kor, eng, math = map(str, input().split())
#     kor, eng, math = int(kor), int(eng), int(math)
#     list.append((name, kor, eng, math))

# list.sort(key=lambda x: (x[1], x[2], x[3], x[0]))

# for i in list:
#     print(i[0])

# n = int(input())
# list = []

# for _ in range(n):
#     name, kor, eng, math = map(str, input().split())
#     kor, eng, math = int(kor), int(eng), int(math)
#     list.append((name, kor, eng, math))

# list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# for i in list:
#     print(i[0])


############# 10989 수 정렬하기3 ############
# 메모리 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# list = []
# for _ in range(n):
#     list.append(int(input()))
# list.sort()

# for i in list:
#     print(i)

# sol 2. 배열로 몇번 등장했는지 확인해서 출력하자
# import sys
# input = sys.stdin.readline
# MAX = 10001       # 10000으로하니까 런타임에러 (2번 발생)
# n = int(input())
# dic = [0] * MAX

# for _ in range(n):
#     num = int(input())
#     dic[num] = dic[num] + 1

# for i in range(MAX):
#     if dic[i] != 0:
#         for j in range(dic[i]):
#             print(i)


############# 11652 카드 ############
# sol 1. 음수 처리 불가능
# import sys
# input = sys.stdin.readline

# n = int(input())
# dic = [0] * 1000000

# for _ in range(n):
#     num = int(input())
#     dic[num] = dic[num] + 1

# big = dic[0]
# ans = 0

# for i in range(len(dic)):
#     if(big < dic[i]):
#         big = dic[i]
#         ans = i

# print(ans)

# sol 2 딕셔너리 사용
# import sys
# input = sys.stdin.readline

# n = int(input())
# dic = {}

# for _ in range(n):
#     card = int(input())
#     if card not in dic:
#         dic[card] = 1
#     else:
#         dic[card] += 1

# # print(dic)
# dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
# # print('dic : ', dic)

# print(dic[0][0])

############# 11004 K번째 수 ############
# import sys
# input = sys.stdin.readline

# n, st = map(int, input().split())
# list = list(map(int, input().split()))

# list.sort()
# print(list[st-1])

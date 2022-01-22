# # 10950
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)

# # 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# 10952
# a, b = 1, 1
# while (a != 0 and b != 0):
#     a, b = map(int, input().split())
#     if(a != 0 and b != 0):
#         print(a+b)

# 10953
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split(','))
#     print(a+b)

# 11021
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print("Case #%s : %s" % (i+1, a+b))

# 11022
# T = int(input())

# for i in range(T):
#     a, b = map(int, input().split())
#     print("Case #%s : %s + %s = %s" % (i+1, a, b, a+b))

# 11718
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# 11719
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# 11720   숫자의 합
# n = input()
# print(sum(map(int, input())))

# 11721   열 개씩 끊어 출력하기
# string = input()

# for i in range(0, len(string), 10):
#     print(string[i:i+10])

# 2741   N 찍기
# N = int(input())

# for i in range(N):
#     print(i+1)

# 2742   기찍 N
# N = int(input())

# for i in range(N, 0, -1):
#     print(i)

# 2739   구구단
# dan = int(input())

# for i in range(1, 10, 1):
#     print("%s * %s = %s" % (dan, i, dan*i))

# 1924   2007년 indent error로 1회 실패, Thu 스펠링 에러로 2회 실패
# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?
# 이를 알아내는 프로그램을 작성하시오.
# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다.
# 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 1월 1일 = 월
# 3월 14일 = 수

# mon, day = map(int, input().split())
# mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# total_days = sum(mons[0:mon-1])+day

# result = total_days % 7

# print(days[result])

# 8393   합
# a = int(input())
# sum = 0
# for i in range(1, a+1):
#     sum += i

# print(sum)


# 10818   최소, 최대
# N = int(input())
# arr = list(map(int, input().split()))

# print(max(arr), min(arr))

# 2438   별 찍기 - 1
# N = int(input())

# for i in range(1, N+1):
#     print('*' * i)

# 2439   별 찍기 - 2
# N = int(input())

# for i in range(1, N+1):
#     print(' ' * (N-i) + '*' * i)

# 2440   별 찍기 - 3
# N = int(input())

# for i in range(N, 0, -1):
#     print(' ' * (N - i) + '*' * i)

# 2441   별 찍기 - 4
# 2442   별 찍기 - 5
# N = int(input())

# for i in range(1, N+1):
#     print(' ' * (N - i) + '*' * (2*i-1))

# 2443   별 찍기 - 6
# N = int(input())

# for i in range(N, 0, -1):
#     print(' ' * (N - i) + '*' * (2*i-1))

# 2444   별 찍기 - 7
# N = int(input())

# for i in range(1, N+1):
#     print(' ' * (N - i) + '*' * (2*i-1))

# for i in range(N-1, 0, -1):
#     print(' ' * (N - i) + '*' * (2*i-1))


# 2445   별 찍기 - 8
# N = int(input())

# for i in range(1, N+1):
#     print('*' * i + ' ' * 2 * (N-i) + '*' * i)
# for i in range(N-1, 0, -1):
#     print('*' * i + ' ' * 2 * (N-i) + '*' * i)

# 2446   별 찍기 - 9
# N = int(input())

# for i in range(N, 0, -1):
#     print(' ' * (N-i) + '*' * (2*i-1))

# for i in range(2, N+1):
#     print(' ' * (N-i) + '*' * (2*i-1))


# 2522   별 찍기 - 12
# N = int(input())

# for i in range(1, N+1):
#     print(' ' * (N-i) + '*' * i)

# for i in range(1, N):
#     print(' ' * (i) + '*' * (N-i))

# 10991   별 찍기 - 16
N = int(input())
# 한 줄에 2n-1개가 들어가야한다.
# 3이면 5이고 구성이 2 1 2
# 4면 7이고 구성이 3 1 3

for i in range(1, N+1):
    print(' ' * (N-i) + '* ' * i)

# 10992   별 찍기 – 17

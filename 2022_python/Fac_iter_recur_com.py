import time
import sys
sys.setrecursionlimit(10**9)


def fac_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def fac_recur(n):
    if n <= 1:
        return 1
    return n * fac_recur(n-1)


a, b = map(int, input().split())
avg = 0
print("입력된 값 : ", a, "반복 횟수 : ", b)
for _ in range(b):
    start_it = time.time()
    fac_iter(a)
    end_it = time.time()
    it_time = end_it-start_it
    print("반복 구현 소요시간 : ", it_time)

    start_re = time.time()
    fac_recur(a)
    end_re = time.time()
    re_time = end_re-start_re
    print("재귀 구현 소요시간 : ", re_time)
    print("시간 차이 : ", re_time - it_time)
    avg = avg + re_time - it_time

print("Summary")
print("test case:", a, "반복 횟수:", b)
print("차이의 평균 :", avg/b * 1000, "ms")
# test case
# 1950  입력시 재귀가 조금 더 오래걸림
# 1900  입력시 차이가 큼

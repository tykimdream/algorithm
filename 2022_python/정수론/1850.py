# 22.02.10 1850

# 모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.
# 예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.

# from math import gcd
# x, y = 0, 0
# a, b = map(int, input().split())

# for _ in range(a):
#     x = x*10+1

# for _ in range(b):
#     y = y*10+1

# a = x
# b = y

# # print("a, b : ", a, b, gcd(a, b))
# print(gcd(a, b))
# 마지막 케이스에 돌아가지 않음
# 500000000000000000 500000000000000002

from math import gcd
A, B = map(int, input().split())
print('1' * gcd(A, B))

print(gcd(500000000000000000, 500000000000000002))
# 다시 풀어보기

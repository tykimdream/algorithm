# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다.
# 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다.
# 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다.
# x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# ex)
# 1 : 1 = 1
# 2 : 1 + (1+2) = 4
# 3 : 1 + (1+2) + (1+3) = 8
# 4 : 1 + (1+2) + (1+3) + (1+2+4) = 15

# 1. 약수 구하기
# 2. 이전 약수와 합이 다음 g(x)

# 1. 약수 구하기

# n = int(input())
# divisor = 0

# for i in range(1, n+1):
#     if(n % i == 0):
#         divisor += i

# print(divisor)

# 2. 이전 약수와 합을 구하기

# n = int(input())

# divisor = 0
# sum = 0

# for i in range(1, n+1):
#     divisor = 0
#     for j in range(1, i+1):
#         if(i % j == 0):
#             divisor += j
#     sum += divisor
#     print(i, '의 약수의 합:', divisor)

# print(sum)

# final
# 시간초과

# n = int(input())

# divisor = 0
# sum = 0

# for i in range(1, n+1):
#     divisor = 0
#     for j in range(1, i+1):
#         if(i % j == 0):
#             divisor += j
#     sum += divisor
#     # print(i, '의 약수의 합:', divisor)

# print(sum)

n = int(input())

sum = 0
for i in range(1, n + 1):
    # 1부터 n 범위내에서 i의 배수의 개수 = 1부터 n의 범위내에서 i를 약수로 가지는 개수(n을 i로 나눈 몫)
    # 예를들면 1부터 100 까지 11의 배수의 개수는 11,22,33...99 까지 9개 = (100 // 11)
    sum += (n // i) * i

print(sum)

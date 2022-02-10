# 22.02.10 9613

# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
from math import gcd

t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    sum = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            sum += gcd(arr[j], arr[k])
    print(sum)

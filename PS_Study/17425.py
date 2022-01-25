# 17427 확장판

# 17427 코드 이용하니 시간 초과
# n = int(input())

# for i in range(n):
#     num = int(input())
#     sum = 0
#     for j in range(1, num+1):
#         sum += (num//j) * j
#     print(sum)

# 다른 방법 필요
# 접근1: g(x)를 저장해나가자 - 시간 복잡도 유사

# 접근2: sol 참고, 배수의 원리

import sys
input = sys.stdin.readline

# 최대값 설정
MAX = 1000000

# DP 1로 초기화
# f(x)
dp = [1] * (MAX+1)

# S: 값 누적 리스트
# g(x)
s = [0] * (MAX+1)


for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        # i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    # g(x) = g(x-1) + f(x)
    s[i] = s[i-1]+dp[i]

n = int(input())
ans = []
for _ in range(n):
    a = int(input())
    ans.append(s[a])

print("\n".join(map(str, ans))+'\n')

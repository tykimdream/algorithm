# https://www.acmicpc.net/problem/11726

n = int(input())

dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n])

# 인혁이 코드
# def main():
#     tile = int(input())

#     d = [0] * tile

#     # 타일이 1개 일 때 경우의 수 1
#     d[0] = 1

#     # 타일이 2개 일 때 경우의 수 2
#     d[1] = 2

#     for i in range(2, tile):
#         d[i] = d[i-1] + d[i-2]

#     # 마지막 타일의 경우의 수 출력
#     print(d[-1] % 10007) # 문제 조건

# # main함수 호출
# main()

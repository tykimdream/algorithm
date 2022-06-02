# import sys
# input = sys.stdin.readline

# # N,M,S, V[] 입력받기
# N, S, M = map(int, input().split())
# V = list(map(int, input().split()))

# # i: N, j: M+1 크기의 dp 배열 만들기
# dp = [[False] * (M+1) for _ in range(N)]

# # S랑 V[0] 적용해서 dp[0]값 초기화
# if S-V[0] >= 0:
#     dp[0][S-V[0]] = True
# if S+V[0] <= M:
#     dp[0][S+V[0]] = True

# # i: 1~N-1, j: 0~M 순차적으로 i번째 곡에서 j 볼륨으로 연주 가능한지 확인 (중간에 연주 불가능한 케이스 예외처리)
# for i in range(1, N):
#     for j in range(M+1):
#         # j 볼륨에서 V[i]만큼 줄인 볼륨이 i-1번째 곡에서 연주 가능했으면 i번째 곡에서 j 볼륨으로도 연주 가능.
#         if j-V[i] >= 0 and dp[i-1][j-V[i]] is True:
#             dp[i][j] = True
#         # j 볼륨에서 V[i]만큼 높인 볼륨이 i-1번째 곡에서 연주 가능했으면 i번째 곡에서 j 볼륨으로도 연주 가능.
#         if j+V[i] <= M and dp[i-1][j+V[i]] is True:
#             dp[i][j] = True
#         # i번째 곡 연주 불가능한 케이스 확인
#         if j == M+1 and True not in dp[i]:
#             print(-1)
#             exit()

# # # dp의 마지막 배열을 뒤집어서 처음 나오는 True의 index값을 M에서 빼면 마지막 곡에서 연주 가능한 최대 볼륨
# dp[N-1].reverse()
# print(M-dp[N-1].index(True))

# # ans = -1
# # for i in range(M, -1, -1):
# #     if dp[N][i] == True:
# #         ans = i
# #     break

# # print(ans)

import sys
input = sys.stdin.readline

# N,M,S, V[] 입력받기
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

# i: N, j: M+1 크기의 dp 배열 만들기
dp = [[False] * (M+1) for _ in range(N)]

# S랑 V[0] 적용해서 dp[0]값 초기화
if M >= S-V[0] >= 0:
    dp[0][S-V[0]] = True
if 0 <= S+V[0] <= M:
    dp[0][S+V[0]] = True

# i: 1~N-1, j: 0~M 순차적으로 i번째 곡에서 j 볼륨으로 연주 가능한지 확인 (중간에 연주 불가능한 케이스 예외처리)
for i in range(1, N):
    for j in range(M+1):
        # j 볼륨에서 V[i]만큼 줄인 볼륨이 i-1번째 곡에서 연주 가능했으면 i번째 곡에서 j 볼륨으로도 연주 가능.
        if 0 <= j-V[i] <= M and dp[i-1][j-V[i]] is True:
            dp[i][j] = True
        # j 볼륨에서 V[i]만큼 높인 볼륨이 i-1번째 곡에서 연주 가능했으면 i번째 곡에서 j 볼륨으로도 연주 가능.
        if 0 <= j+V[i] <= M and dp[i-1][j+V[i]] is True:
            dp[i][j] = True

        # i번째 곡 연주 불가능한 케이스 확인
        if j == M+1 and True not in dp[i]:
            print(-1)
            exit()

# dp의 마지막 배열을 뒤집어서 처음 나오는 True의 index값을 M에서 빼면 마지막 곡에서 연주 가능한 최대 볼륨
for i in range(M, -1, -1):
    if dp[N-1][i] is True:
        print(i)
        exit()
print(-1)

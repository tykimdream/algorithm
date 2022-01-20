# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# # 시간초과
# M, N = map(int, input().split())

# for i in range(M, N+1):
#     flag = 0
#     if(i == 0):
#         continue
#     for j in range(2, i):
#         if(i % j == 0):
#             flag += 1
#     if(flag == 0):
#         print(i)

M, N = map(int, input().split())

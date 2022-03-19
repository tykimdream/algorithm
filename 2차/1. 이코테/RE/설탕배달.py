# 2839
# target = int(input())
# dp = [0 for _ in range(target)]
# print(dp)
# for i in range(3, target+1):
#     if i / 3 == i // 3:
#         dp[i] = i/3
#     elif i / 5 == i // 5:
#         dp[i] = i//5
#     else:
#         dp[i] = 0

#     if dp[i-3] != 0 and dp[i-3] > 0:
#         dp[i] = min(dp[i], dp[i-3]+1)
#     if dp[i-5] != 0 and dp[i-5] > 0:
#         dp[i] = min(dp[i], dp[i-5]+1)

# print(dp)

num = int(input())
count = 0
while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)

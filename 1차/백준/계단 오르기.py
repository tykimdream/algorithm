n = int(input())

step = []
for _ in range(n):
    step.append(int(input()))

dp = []
dp.append(step[0])
dp.append(max(step[0]+step[1], step[1]))
dp.append(max(step[0]+step[2], step[1]+step[2]))

for i in range(3, n):
    dp.append(max(dp[i-2]+step[i], dp[i-3]+step[i]+step[i-1]))

print(dp.pop())

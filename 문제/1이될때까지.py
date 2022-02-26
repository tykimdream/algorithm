n, k = map(int, input().split())

count = 0
while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

print(count)

# Sol
n, k = map(int, input().split())
result = 0

while True:
    # 나누기 하기 전까지 빼기를 이렇게 하면 효율적
    target = (n//k) * k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

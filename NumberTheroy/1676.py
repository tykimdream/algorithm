n = int(input())
total = 1
for i in range(1, n+1):
    total *= i

total = list(reversed(str(total)))
result = 0
for i in total:
    if i == '0':
        result += 1
    else:
        break

print(result)
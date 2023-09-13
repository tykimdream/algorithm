number = list(map(int, input()))

sum = number[0]
for i in range(1, len(number)):
    if sum <= 1 or sum <= 1:
        sum += number[i]
    else:
        sum = sum * number[i]

print(sum)

money = int(input())
count = 0
rest = [500, 100, 50, 10]

for coin in rest:
    count += money // coin
    money %= coin

print(count, "개의 동전")

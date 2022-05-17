Money = int(input())
count = 0
coin = [500, 100, 50, 10]

for i in coin:
    count += Money // i
    Money %= i

print(count, "개 반환")





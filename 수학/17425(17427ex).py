size = int(input())

# for j in range(0, size):
#     n = int(input())

#     sum = 0
#     for i in range(1, n + 1):
#         sum += (n // i) * i
#     print(sum)

while True:
    try:
        n = int(input())
    except:
        break
    sum = 0
    for i in range(1, n + 1):
        sum += (n // i) * i
    print(sum)

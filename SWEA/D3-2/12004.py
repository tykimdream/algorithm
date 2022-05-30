dic = []
for i in range(1, 10):
    for j in range(1, 10):
        dic.append(i*j)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    if n in dic:
        result = "Yes"
    else:
        result = "No"

    print("#{} {}".format(tc, result))
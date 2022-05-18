num = int(input())
result = []

for i in range(1, num + 1):
    if str(i).count('3') or str(i).count('6') or str(i).count('9'):
        result.append('-' * (str(i).count('3') + str(i).count('6') + str(i).count('9')))
    else:
        result.append(i)

for i in result:
    print(i, end=' ')
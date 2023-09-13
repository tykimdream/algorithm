s = input()

ans = []
num = 0
for i in s:
    if i.isalpha():
        ans.append(i)
    else:
        num += int(i)

ans.sort()
ans.append(str(num))
print(''.join(ans))

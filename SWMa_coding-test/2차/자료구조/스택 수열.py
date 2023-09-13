# 1874

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(int(input()))


n = int(input())
count = 0
stack = []
result = []
no_message = True

for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        no_message = False


if no_message == False:
    print("NO")
else:
    print("\n".join(result))

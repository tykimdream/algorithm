# 22.1.28 10799
# 쇠막대기

import sys
input = sys.stdin.readline

bar = list(input().strip())
answer = 0
stack = []
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')

    else:  # )이 나오면
        if bar[i-1] == '(':
            stack.pop()
            answer = answer + len(stack)
        else:
            stack.pop()
            answer = answer + 1  # 끄트머리 막대기 부분을 더해준다.

print(answer)

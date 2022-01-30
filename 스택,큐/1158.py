# 22.01.30 1158
# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 7 3
# <3, 6, 2, 7, 5, 1, 4>

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

ans = []
exe = 0

for t in range(n):
    exe += k-1
    if (exe >= len(arr)):
        exe = exe % len(arr)

    ans.append(str(arr.pop(exe)))
    # 출력되나 확인
    # print(t+1, "회차 : ", "arr : ", arr, "ans : ", ans)

print("<", ", ".join(ans)[:], ">", sep='')

# size, k = map(int, input().split())

# arr = [i for i in range(1, size+1)]

# answer = []
# num = 0

# for _ in range(size):
#     num += k-1
#     if num >= len(arr):
#         num = num % len(arr)

#     answer.append(str(arr.pop(num)))

# print("<", ", ".join(answer)[:], ">", sep="")

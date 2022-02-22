# https://www.acmicpc.net/problem/2606
from collections import deque
n = int(input())
e = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(arr, visited, v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in arr[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


visited = [False] * (n+1)

bfs(arr, visited, 1)
print(visited.count(True)-1)

# 시간을 비교해보면 DFS가 더 빠르다는 것을 알 수 있다.

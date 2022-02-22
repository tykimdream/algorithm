# https://www.acmicpc.net/problem/11724
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 인접 행렬 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


count = 0

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        bfs(i)
        count += 1
print(count)

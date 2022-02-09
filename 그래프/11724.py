# 22.02.08 11724

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 인접 리스트 구현
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

amount = 0

for i in range(1, n+1):
    if not visited[i]:
        amount += 1
        dfs(graph, i, visited)

print(amount)

# 런타임 에러 발생
# import sys한다음 limit를 걸어주니 해결

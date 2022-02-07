# 22.02.04 1260
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

from collections import deque
import sys
input = sys.stdin.readline

# DFS, BFS 메소드 각각 구현


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 메인문 구현
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph.sort()
# print(graph)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)

# feedback
# 정렬을 한번 해야 정답이 나왔는데 어떻게 할까 하고 sort부터해보니 안되서
# 함수 안에 삽입했는데 우려와 달리 맞게 돌아갔다
# 시간 복잡도가 많이 올라갈거라고 생각하고 다른 방법이 있나 알아봐야겠다.

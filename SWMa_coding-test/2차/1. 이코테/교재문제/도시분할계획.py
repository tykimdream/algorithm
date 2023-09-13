def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(0, v+1):
    parent[i] = i

# 간선을 담을 리스트
edges = []
result = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    # a - b로 가는 c의 비용
    # 우리는 c를 기준으로 정렬할 에정이기 때문에
    # c를 먼저 넣는다.
    edges.append((c, a, b))

edges.sort()
last = 0  # MST에 포함되는 간선중 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        last = cost

print(result - last)

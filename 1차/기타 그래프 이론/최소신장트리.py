# Spanning tree (사이클이 없는 그래프)
# 대표적인 최소 신장 트리
# 크루스칼 알고리즘

# Rule
# 간선 데이터를 오름차순으로 정렬
# 간선을 하나씩 확인하며 사이클을 발생시키는지 확인
# 발생하지 않는 경우 트리에 포함시킨다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


e, v = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for i in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위하여 튜플의 첫 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort(key=lambda x: x[0])

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parent(parent, a, b)
        result += cost

print(result)

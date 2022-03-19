v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


edges = []
result = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        last = cost

print(result, cost)
print(result - last)

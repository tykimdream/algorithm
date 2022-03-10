from gettext import find


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

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        # 사이클 발생하면 종료
        cycle = True
        break
    else:
        # 사이클 발생하지 않으면 유니온 진행
        union_parent(parent, a, b)

if cycle:
    print("무방향 그래프에서 사이클이 존재합니다.")
else:
    print("사이클이 존재하지 않습니다.")

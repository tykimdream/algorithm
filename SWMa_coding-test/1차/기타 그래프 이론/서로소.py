# 특정 원소가 속한 집합을 찾기
# 루트 번호를 반환하는 함수이다.
def find_parent(parent, x):  # 부모테이블, 노트의 번호
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모 테이블 초기화하기

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기
print('부모 테이블 : ', end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")


# 이 경우 선형적으로 뒤에서부터 호출되면 시간 복잡도가 높음
# 경로 압축사용

# Sol
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

import heapq

# 오름차순 힙 정렬


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("최소 힙 : ", result, "\n")


def max_heap(iterable):
    h = []
    result = []
    # 데이터 삽입시 부호를 바꿔서 삽입하고
    for value in iterable:
        heapq.heappush(h, -value)
    # 데이터를 꺼낼때 다시 부호를 바꾸면
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    # MAX_HEAP이 완성된다
    return result


result = max_heap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("최대 힙 : ", result, "\n")

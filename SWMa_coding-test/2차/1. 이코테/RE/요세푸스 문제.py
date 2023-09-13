# 1158
# 형식 맞추기, 나눠지는 수 기준 잡기 두개 다시 봐야함
n, k = map(int, input().split())

graph = [i for i in range(1, n+1)]
result = []
# print(graph)
num = 0

for i in range(n):
    num += k-1
    if num >= len(graph):
        num = num % len(graph)

    result.append(str(graph.pop(num)))

print("< ", ', '.join(result), " >", sep="")

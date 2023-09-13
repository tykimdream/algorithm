import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []
DNA = []
for _ in range(n):
    DNA.append(input().rstrip())

print(DNA)
for i in range(n):
    count = 0
    for j in range(n):
        for k in range(m):
            if DNA[i][j] != DNA[j][k]:
                count += 1

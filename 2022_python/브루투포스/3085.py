size = int(input())
max = 0

c = [input() for i in range(size)]

for i in range(size):
    for j in range(size):
        if(c[i][i] != c[i][j]):
            c[i][i], c[i][j] = c[i][j], c[i][i]

size = int(input())
max = 0

c = [input() for i in range(size)]

for i in range(size):
    for j in range(size):
        if(c[i] != c[j]):
            c[i], c[j] = c[j], c[i]

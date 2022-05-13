index = int(input())
source = list(map(int, input().split()))

source.sort()
middle = round(index/2)
print(source[middle-1])

# import sys
T = int(input())
print(T)
for test_case in range(1, T+1):
    arr = input()
    sample = list(arr)
    sample_comp = list(reversed(sample))
    result = 0
    if sample == sample_comp:
        result = 1
    else:
        result = 0
    print("#{} {}".format(test_case, result))

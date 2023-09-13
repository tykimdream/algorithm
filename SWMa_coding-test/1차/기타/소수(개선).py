import math


def is_Prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


print(is_Prime(4))
print(is_Prime(7))

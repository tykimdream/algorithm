def is_Prime(target):
    for i in range(2, target):
        if target % i == 0:
            print(target, ": 소수가 아닙니다")
            return False
    print(target, ": 소수입니다")
    return True


prime = 0
for i in range(3, 100):
    if is_Prime(i) == True:
        prime += 1

print(prime)

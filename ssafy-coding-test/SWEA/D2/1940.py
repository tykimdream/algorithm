T = int(input())

for tc in range(1, T+1):
    command = int(input())
    current_speed = 0
    distance = 0
    for _ in range(command):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            current_speed += arr[1]
        elif arr[0] == 2:
            if arr[1] > current_speed:
                current_speed = 0
            else:
                current_speed -= arr[1]
        distance += current_speed
    print("#{} {}".format(tc, distance))
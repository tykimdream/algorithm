# 22.02.10 4963

# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = []
    for i in range(h):
        island.append(list(map(int, input().split())))

    print(island)

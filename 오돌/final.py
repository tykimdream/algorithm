n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]


def countPaths(maze, i, j, dest, visited):

    # if destination (x, y) is found, return 1
    if (i, j) == dest:
        return 1

    # stores number of unique paths from source to destination
    count = 0

    # mark the current cell as visited
    visited[i][j] = True

    # if the current cell is a valid and open cell
    if 0 <= i < n and 0 <= j < m and maze[i][j] == 1:

        # go down (i, j) ——> (i + 1, j)
        if i + 1 < n and not visited[i + 1][j]:
            count += countPaths(maze, i + 1, j, dest, visited)

        # go up (i, j) ——> (i - 1, j)
        if i - 1 >= 0 and not visited[i - 1][j]:
            count += countPaths(maze, i - 1, j, dest, visited)

        # go right (i, j) ——> (i, j + 1)
        if j + 1 < m and not visited[i][j + 1]:
            count += countPaths(maze, i, j + 1, dest, visited)

        # go right down (i, j) ——> (i+1, j+1)
        if j + 1 < m and i + 1 < n and not visited[i+1][j + 1]:
            count += countPaths(maze, i+1, j + 1, dest, visited)

    # backtrack from the current cell and remove it from the current path
    visited[i][j] = False

    return count


# destination cell
dest = (n-1, m-1)

print("The total number of unique paths are",
      countPaths(arr, 0, 0, dest, visited))

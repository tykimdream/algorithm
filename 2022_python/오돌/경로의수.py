# def isValidCell(x, y):
#     return not (x < 0 or y < 0 or x >= n or y >= m)


# def countPaths(maze, i, j, dest, visited):

#     # if destination (x, y) is found, return 1
#     if (i, j) == dest:
#         return 1

#     # stores number of unique paths from source to destination
#     count = 0

#     # mark the current cell as visited
#     visited[i][j] = True

#     # if the current cell is a valid and open cell
#     if isValidCell(i, j) and maze[i][j] == 1:

#         # go down (i, j) ——> (i + 1, j)
#         if i + 1 < n and not visited[i + 1][j]:
#             count += countPaths(maze, i + 1, j, dest, visited)

#         # go up (i, j) ——> (i - 1, j)
#         if i - 1 >= 0 and not visited[i - 1][j]:
#             count += countPaths(maze, i - 1, j, dest, visited)

#         # go right (i, j) ——> (i, j + 1)
#         if j + 1 < m and not visited[i][j + 1]:
#             count += countPaths(maze, i, j + 1, dest, visited)

#         # go right down (i, j) ——> (i+1, j+1)
#         if j + 1 < m and i + 1 < n and not visited[i+1][j + 1]:
#             count += countPaths(maze, i+1, j + 1, dest, visited)

#     # backtrack from the current cell and remove it from the current path
#     visited[i][j] = False

#     return count


# def findCount(maze, src, dest):

#     # get source cell (i, j)
#     i, j = src

#     # get destination cell (x, y)
#     x, y = dest


#     # 2D matrix to keep track of cells involved in the current path
#     visited = [[False] * m for _ in range(n)]

#     # start from source cell (i, j)
#     return countPaths(maze, i, j, dest, visited)


# if __name__ == '__main__':

#     n, m = map(int, input().split())
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().split())))

#     # source cell
#     src = (0, 0)

#     # destination cell
#     dest = (n-1, m-1)

#     print("The total number of unique paths are", findCount(arr, src, dest))

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


if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    # destination cell
    dest = (n-1, m-1)

    print("The total number of unique paths are",
          countPaths(arr, 0, 0, dest, visited))

# Python3

def spiralNumbers(n):
    matrix = [[0] * n for i in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = 0, 0
    i = 0
    dr, dc = dirs[i]
    for num in range(1, n * n + 1):
        matrix[r][c] = num
        newR, newC = r + dr, c + dc
        if (0 <= newR < n) and (0 <= newC < n) and (matrix[newR][newC] == 0):
            r, c = newR, newC
            continue
        i = (i + 1) % len(dirs)
        dr, dc = dirs[i]
        r, c = r + dr, c + dc

    return matrix

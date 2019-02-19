# Python - 2.7.6

live_rule = {
    0: [3],
    1: [2, 3]
}

dirs = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
]

def next_gen(cells):
    if len(cells) == 0:
        return []
    N, M = len(cells), len(cells[0])
    next = [[0] * M  for i in range(N)]

    for row in range(N):
        for col in range(M):
            num = 0
            for dc, dr in dirs:
                r, c = row + dr, col + dc
                if (0 <= r < N) and (0 <= c < M):
                    num += cells[r][c]
            next[row][col] = 1 if num in live_rule[cells[row][col]] else 0
    return next

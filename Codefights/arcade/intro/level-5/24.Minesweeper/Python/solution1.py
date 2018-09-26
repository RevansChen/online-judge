# Python3

def minesweeper(matrix):
    vecs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    results = [ [0] * len(m) for m in matrix ]
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c]:
                for dr, dc in vecs:
                    if (0 <= (r + dr) < len(matrix)) and (0 <= (c + dc) < len(matrix[0])):
                        results[r + dr][c + dc] += 1

    return results

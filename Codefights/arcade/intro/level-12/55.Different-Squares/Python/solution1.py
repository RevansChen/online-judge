# Python3

def differentSquares(matrix):
    squares = set()

    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            if (0 <= r + 1 < len(matrix)) and (0 <= c + 1 < len(matrix[0])):
                squares.add(','.join(map(str, matrix[r][c:c + 2] + matrix[r + 1][c:c + 2])))
    return len(squares)

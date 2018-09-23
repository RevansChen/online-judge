# Python3

def chessKnight(cell):
    col, row = ord(cell[0]) - ord('a'), int(cell[1]) - 1
    count = 0
    for c, r in [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (2, 1), (-2, -1), (2, -1)]:
        if 0 <= (col + c) < 8 and 0 <= (row + r) < 8:
            count += 1
    return count

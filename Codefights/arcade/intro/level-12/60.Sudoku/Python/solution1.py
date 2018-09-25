# Python3

from itertools import chain

def sudoku(grid):
    for row in grid:
        if len(set(row)) != 9:
            return False
    for col in zip(*grid):
        if len(set(col)) != 9:
            return False
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            subGrid = [*chain.from_iterable(grid[r + i][c:c + 3] for i in range(3))]
            if len(set(subGrid)) != 9:
                return False
    return True


# coding: utf-8
# Python3
def sudoku2(grid):
    def valid(nums):
        nums = [ n for n in nums if n != '.' ]
        numSet = set(nums)
        return len(nums) == len(numSet)
    
    for row in grid:
        if not valid([ n for n in row ]):
            return False
    for colIdx in range(9):
        if not valid([ grid[rowIdx][colIdx] for rowIdx in range(9) ]):
            return False
    for colOffset in range(0, 9, 3):
        for rowOffset in range(0, 9, 3):
            nums = []
            for rowIdx in range(rowOffset, rowOffset + 3):
                nums.extend(grid[rowIdx][colOffset:colOffset+3])
            if not valid(nums):
                return False
    return True

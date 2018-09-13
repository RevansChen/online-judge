# Python3

def chessBoardCellColor(cell1, cell2):
    getColor = lambda cell: (ord(cell[0]) - ord('A') + int(cell[1])) & 1
    return getColor(cell1) == getColor(cell2)

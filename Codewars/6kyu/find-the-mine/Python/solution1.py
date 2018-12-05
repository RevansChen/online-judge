# Python - 3.6.0

def mineLocation(field):
    row, col = 0, 0
    for row in range(len(field)):
        if 1 in field[row]:
            col = field[row].index(1)
            break
    return [row, col]

import sys

def flip(row, col, arr):
    for r in range(row // 2):
        for c in range(col):
            idx1, idx2 = r * col + c, (row - r - 1) * col + c
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

def rotate(row, col, arr):
    newArray = []
    for c in range(col - 1, -1, -1):
        newArray.extend(arr[c::col])
    return (col, row, newArray)

def printAnswer(row, col, arr):
    print('%d %d' % (row, col))
    for r in range(row):
        print(' '.join(arr[r * col:(r + 1) * col]))

lines = sys.stdin.readlines()
while lines:
    row, col, num = [*map(int, lines.pop(0).split(' '))]
    arr = []
    for i in range(row):
        arr.extend([*map(str.strip, lines.pop(0).split(' '))])
    ops = [*map(int, lines.pop(0).split(' '))]
    while ops:
        op = ops.pop()
        if op:
            flip(row, col, arr)
        else:
            row, col, arr = rotate(row, col, arr)
    printAnswer(row, col, arr)

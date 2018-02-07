# coding: utf-8
# Python3
def rotateImage(a):
    n = len(a)
    return [ [ a[row][col] for row in range(n - 1, -1, -1) ] for col in range(n) ]

# Python3

def sortByHeight(a):
    trees = sorted(e for e in a if e >= 0)
    pos = 0
    for i in range(len(a)):
        if a[i] >= 0:
            a[i] = trees[pos]
            pos += 1
    return a

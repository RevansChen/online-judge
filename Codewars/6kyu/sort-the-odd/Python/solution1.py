# Python - 3.4.3

def sort_array(sourceArray):
    indexes = []
    odds = []
    for i, e in enumerate(sourceArray):
        if e & 1:
            indexes.append(i)
            odds.append(e)
    odds.sort()
    for i, e in zip(indexes, odds):
        sourceArray[i] = e
    return sourceArray

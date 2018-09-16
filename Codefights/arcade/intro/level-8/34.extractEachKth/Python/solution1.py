# Python3

def extractEachKth(inputArray, k):
    return [ e for i, e in enumerate(inputArray) if (i + 1) % k ]

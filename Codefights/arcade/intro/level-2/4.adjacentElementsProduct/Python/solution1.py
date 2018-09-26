# Python3

def adjacentElementsProduct(inputArray):
    a, b = inputArray[:2]
    maxma = a * b
    a = b
    for b in inputArray[2:]:
        maxma = max(maxma, a * b)
        a = b
    return maxma

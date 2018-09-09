# Python3

def avoidObstacles(inputArray):
    from functools import reduce
    for i in range(2, max(inputArray)):
        if reduce(lambda x, y: x and y, [ bool(e % i) for e in inputArray ]):
            return i
    return max(inputArray) + 1

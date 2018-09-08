# Python3

def arrayMaximalAdjacentDifference(inputArray):
    return max(max(inputArray[i - 1:i + 1]) - min(inputArray[i - 1:i + 1]) for i in range(1, len(inputArray)))

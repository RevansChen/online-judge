# Python3

def arrayMaxConsecutiveSum(inputArray, k):
    def __inner():
        total = sum(inputArray[:k])
        yield total
        for i in range(1, len(inputArray) - (k - 1)):
            total += inputArray[i + k - 1] - inputArray[i - 1]
            yield total
    return max(__inner())

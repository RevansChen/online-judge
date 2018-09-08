# Python3

def arrayChange(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        if inputArray[i - 1] >= inputArray[i]:
            val = (inputArray[i - 1] - inputArray[i]) + 1
            count += val
            inputArray[i] += val
    return count

# Python3

def diffOne(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count == 2:
            return False
    return bool(count)

def func(inputArray, curr):
    if len(inputArray) == 1:
        return diffOne(inputArray[0], curr)
    for i in range(len(inputArray)):
        if diffOne(inputArray[i], curr):
            inputArray[i], inputArray[-1] = inputArray[-1], inputArray[i]
            if func(inputArray[:-1], inputArray[-1]):
                return True
            inputArray[i], inputArray[-1] = inputArray[-1], inputArray[i]
    return False

def stringsRearrangement(inputArray):
    for i in range(len(inputArray)):
        inputArray[i], inputArray[-1] = inputArray[-1], inputArray[i]
        if func(inputArray[:-1], inputArray[-1]):
            return True
        inputArray[i], inputArray[-1] = inputArray[-1], inputArray[i]
    return False

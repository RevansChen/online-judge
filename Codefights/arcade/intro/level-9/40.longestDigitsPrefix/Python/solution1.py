# Python3

def longestDigitsPrefix(inputString):
    for i, e in enumerate(inputString):
        if not e.isnumeric():
            return inputString[:i]
    return inputString

# Python3

def allLongestStrings(inputArray):
    maxLen = max(len(s) for s in inputArray)
    return [ s for s in inputArray if len(s) == maxLen ]

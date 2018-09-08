# Python3

def palindromeRearranging(inputString):
    counts = { c:inputString.count(c) for c in inputString }
    return len([v for v in counts.values() if v % 2]) == len(inputString) % 2

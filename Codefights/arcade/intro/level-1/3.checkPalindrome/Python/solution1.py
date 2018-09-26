# Python3

def checkPalindrome(inputString):
    return inputString[:len(inputString) // 2] == inputString[::-1][:len(inputString) // 2]

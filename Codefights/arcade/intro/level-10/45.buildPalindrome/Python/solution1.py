# Python3

import math

def buildPalindrome(st):
    isPalindrome = lambda s: s[:math.ceil(len(s) / 2)] == s[-math.ceil(len(s) / 2):][::-1]
    adding = ''
    for c in st:
        if isPalindrome(st + adding):
            break
        adding = c + adding
    return st + adding

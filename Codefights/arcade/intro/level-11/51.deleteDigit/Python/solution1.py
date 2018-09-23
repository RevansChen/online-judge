# Python3

def deleteDigit(n):
    s = str(n)
    return max(int(s[:i] + s[i+1:]) for i in range(len(s)))

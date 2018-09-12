# Python3

def alphabeticShift(inputString):
    la = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    return inputString.translate(str.maketrans(la, la[1:] + la[0]))

# Python3

def messageFromBinaryCode(code):
    return ''.join(chr(int(code[i:i + 8], 2)) for i in range(0, len(code), 8))

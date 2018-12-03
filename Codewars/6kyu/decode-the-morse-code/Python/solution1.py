# Python - 2.7.6

def decodeMorse(morseCode):
    morseCode = morseCode.strip(' ').replace('   ', ' % ')
    return ''.join([MORSE_CODE.get(code, ' ') for code in morseCode.split(' ')])

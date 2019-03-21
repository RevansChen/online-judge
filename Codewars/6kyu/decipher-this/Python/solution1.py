# Python - 3.6.0

def decipher_this(string):
    import re
    array = []
    for word in string.split(' '):
        if word:
            ascii, word = re.match(r'(\d+)(.*)', word).groups()
            if len(word) >= 2:
                word = word[-1] + word[1:-1] + word[0]
            array.append(chr(int(ascii)) + word)
    return ' '.join(array)

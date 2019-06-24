# Python - 3.4.3

mirror = lambda code, chars = __import__('string').ascii_lowercase: code.lower().translate(str.maketrans(chars, chars[::-1]))

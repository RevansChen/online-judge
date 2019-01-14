# Python - 3.6.0

def is_uppercase(inp):
    string = ''.join(filter(lambda s: s.isalpha(), inp))
    return string == string.upper()

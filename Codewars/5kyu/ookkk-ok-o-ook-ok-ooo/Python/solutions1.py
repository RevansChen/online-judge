# Python - 3.6.0

def okkOokOo(s):
    t = str.maketrans('okOK!?', '0101\n\n')
    s = s.translate(t)
    s = ''.join(filter(lambda i: i == '0' or i == '1' or i == '\n', s))
    chars = [chr(int(binary, 2)) for binary in s.split('\n') if len(binary) > 0]
    return ''.join(chars)

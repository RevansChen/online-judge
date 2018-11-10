# Python - 2.7.6

def rgb(r, g, b):
    return ''.join('%02X' % max(min(i, 255), 0) for i in [r, g, b])

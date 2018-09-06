# Python3

def addBorder(picture):
    return [ '*' * (len(picture[0]) + 2) ] + [ '*%s*' % s for s in picture ] + [ '*' * (len(picture[0]) + 2) ]

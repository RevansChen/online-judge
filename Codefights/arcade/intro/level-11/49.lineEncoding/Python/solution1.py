# Python3

def lineEncoding(s):
    output = ''
    ch, count = s[0], 1
    for c in s[1:]:
        if c != ch:
            output += ('' if count == 1 else str(count)) + ch
            ch, count = c, 0
        count += 1

    return output + ('' if count == 1 else str(count)) + ch

# Python - 2.7.6

from struct import *

def toAscii85(data):
    paddings = 4 - (len(data) % 4)
    if paddings != 4:
        data += '\0' * paddings
    binarys = unpack(">%dI" % (len(data) // 4), data)
    chunks = []
    for binary in binarys:
        b = binary
        chunk = [0] * 5
        for i in range(4, -1, -1):
            b, chunk[i] = b // 85, chr(b % 85 + 33)
        chunks.append(''.join(chunk))
    if paddings != 4:
        chunks[-1] = chunks[-1][:-paddings]
    return "<~%s~>" % ''.join([chunk if chunk != "!!!!!" else 'z' for chunk in chunks])
    
def fromAscii85(data):
    ascii85 = data[2:-2].replace('z', "!!!!!")
    ascii85 = [c for c in ascii85 if ((ord(c) >= 33) and (ord(c) <= 117))]
    paddings = 5 - (len(ascii85) % 5)
    if paddings != 5:
        ascii85 += 'u' * paddings
    binarys = [ord(b) - 33 for b in ascii85]
    text = ''
    for i in range(0, len(binarys), 5):
        u32 = 0
        for j in range(i, i + 5):
            u32 = u32 * 85 + binarys[j]
        text += pack(">I", u32)
    if paddings != 5:
        return text[:-paddings]
    return text
# Python - 3.4.3

from math import ceil

def createSequence(length):
    size = ceil(length ** 0.5)
    sz = size
    sequence = [-1] * (size ** 2)
    index, depth = 0, 0
    while sz > 0:
        if sz == 1:
            sequence[depth * size + depth] = index
        for i in range(sz - 1):
            sequence[depth * size + (i + depth)] = index
            sequence[(depth + i) * size + (size - depth - 1)] = index + 1
            sequence[(size - 1 - depth) * size + (size - 1 - i - depth)] = index + 2
            sequence[(size - 1 - depth - i) * size + depth] = index + 3
            index += 4
        depth += 1
        sz -= 2
    return sequence

def encode(string):
    seq = createSequence(len(string))
    return ''.join((string[i] if i < len(string) else ' ') for i in seq)

def decode(string):
    seq = createSequence(len(string))
    ls = [ (seq[i], (string[i] if i < len(string) else ' ')) for i in range(len(seq)) ]
    ls.sort(key=lambda x: x[0])
    return ''.join(c for i, c in ls).rstrip()

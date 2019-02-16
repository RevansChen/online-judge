# Python - 3.6.0

def replace_zero(arr):
    s = ''.join(map(str, arr))
    strs = s.split('0')
    maxLength = 0
    left, right = '', ''
    for i in range(len(strs) - 1):
        l, r = strs[i], strs[i + 1]
        if l or r:
            length = len(l) + len(r) + 1
            if length >= maxLength:
                maxLength = length
                left, right = l, r

    return s.index('0', s.rindex(left + '0' + right))

# Python - 3.4.3

def z(iter, num):
    lst = [ [] for i in range(num) ]
    r, dr = 0, 1
    for n in iter:
        lst[r].append(n)
        if (r <= 0 and dr == -1) or (r >= (num - 1) and dr == 1):
            dr *= -1
        r += dr
    result = []
    for e in lst:
        result += e
    return result
            
def encode_rail_fence_cipher(string, n):
    return ''.join(z(string, n))
    
def decode_rail_fence_cipher(string, n):
    lst = [ '' ] * len(string)
    for e, i in zip(string, z(range(len(string)), n)):
        lst[i] = e
    return ''.join(lst)
# Python - 3.4.3

def z(length, num):
    r, sign = 0, True
    for n in range(length):
        yield r, n
        if sign:
            r += 1
            if r >= num:
                r -= 2
                sign = False
        else:
            r -= 1
            if r < 0:
                r += 2
                sign = True
            
def encode_rail_fence_cipher(string, n):
    rails = [ '' for i in range(n) ]
    for r, n in z(len(string), n):
        rails[r] += string[n]
    return ''.join(rails)
    
def decode_rail_fence_cipher(string, n):
    full = 2 * (n - 1)
    groups = len(string) // full
    incomp = len(string) - groups * full
    lengths = [ groups ] + ([ 2 * groups ] * (n - 2)) + [ groups ]
    for r, _ in z(incomp, n):
        lengths[r] += 1

    i, rails = 0, []
    for length in lengths:
        rails.append(list(string[i:i + length]))
        i += length
    
    return ''.join(rails[r].pop(0) for r, _ in z(len(string), n))
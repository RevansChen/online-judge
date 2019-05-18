# Python - 3.6.0

def recaman(n):
    prev, curr = 0, 0
    seq = set()
    for i in range(1, n + 1):
        curr = prev - i
        if curr <= 0 or curr in seq:
            curr = prev + i
        seq.add(curr)
        prev = curr
    return curr

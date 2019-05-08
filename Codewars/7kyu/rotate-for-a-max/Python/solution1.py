# Python - 3.6.0

def max_rot(n):
    s = str(n)
    vals = {n}
    for i in range(len(s)):
        s = s[:i] + s[i + 1:] + s[i]
        vals.add(int(s))
    return max(vals)

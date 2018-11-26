# Python - 3.6.0

def sc(width, length, gaps):
    gaps += 1
    d = ((width - 1) + (length - 1)) * 2
    return (d // gaps) if ((d % gaps) == 0) else 0

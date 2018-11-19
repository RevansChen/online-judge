# Python - 3.6.0

def count(string):
    return { c: string.count(c) for c in set(string) }

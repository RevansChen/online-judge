# Python - 3.6.0

def dative(word):
    for w in word[::-1]:
        if w in 'eéiíöőüű':
            return word + 'nek'
        elif w in 'aáoóuú':
            return word + 'nak'
    return None

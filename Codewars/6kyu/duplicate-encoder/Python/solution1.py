# Python - 3.4.3

def duplicate_encode(word):
    word = word.lower()
    return word.translate({
        ord(char): ord(')' if word.count(char) > 1 else '(') for char in set(word)
    })
    

# Python - 3.4.3

def duplicate_encode(word):
    word = word.lower()
    table = {}
    for char in word:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    result = ''
    for char in word:
        result += '(' if table[char] == 1 else ')'
    
    return result

# Python - 3.4.3

def duplicate_encode(word):
    word = word.lower()

    # 統計每一個字出現的次數
    table = {}
    for char in word:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1

    # 根據字的出現次數輸出'('或')'
    result = ''
    for char in word:
        result += '(' if table[char] == 1 else ')'
    
    return result

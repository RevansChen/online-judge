# Python - 3.4.3

def duplicate_encode(word):
    word = word.lower()
    
    # 利用str的translate()做替換表
    # 當字出現2次以上時替換為')', 只出現1次則替換為'(')
    return word.translate({
        ord(char): ord(')' if word.count(char) > 1 else '(') for char in set(word)
    })
    

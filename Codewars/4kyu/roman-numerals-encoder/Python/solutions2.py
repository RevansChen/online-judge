# Python - 2.7.6

# 列出所有可能的進位值
symbols = [
    (1000, 'M'), 
    (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), 
    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), 
    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def solution(n):
    result = ''
    for number, roman in symbols:
        result += roman * (n // number) # 符號出現次數
        n %= number                     # 剩餘位數
    return result
# Ruby - MRI 2.3.0

def solution(n)
    # 列出所有可能的進位值
    symbols = {
        M: 1000, 
        CM: 900, D: 500, CD: 400, C: 100, 
        XC: 90, L: 50, XL: 40, X: 10, 
        IX: 9, V: 5, IV: 4, I: 1
    }
    
    result = ""
    symbols.each do |roman, number|
        result += roman.to_s * (n / number) # 符號出現次數
        n %= number                         # 剩餘位數
    end
    
    return result
end
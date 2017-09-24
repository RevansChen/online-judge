# Ruby - MRI 2.3.0

def solution(n)
    # 範圍限制，大於等於4000以上的無對應符號，所以不處理
    if n <= 0 or n >= 4000
        return ""
    end
        
    symbols = "IVXLCDM"
    result = ""

    # 轉換方式為
    # 將symbol兩個作為一組，並加上下一組的較小的那一個
    # step   group
    #   1    IV + X
    #   2    XL + C
    #   3    CD + M
    i = 0
    while n > 0
        n, v = n / 10, n % 10   # 剩餘位數, 目前位數
        p5, p1 = v / 5, v % 5   # 計算出5跟1的數量

        r = ""
        if p1 == 4
            # 針對1數量為4個做處理，從加法變減法
            # 小的在前 (I)，大的在後 (V 或 X)
            r = symbols[i] + symbols[i + 1 + p5]
        else
            # 1數量為0~3個的為加法
            if p5 > 0
                r = symbols[i + 1]  # V
            end
            r += symbols[i] * p1    # I, II, III
        end
            
        result = r + result
        i += 2
    end
    
    return result
end
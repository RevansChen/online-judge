# Python - 3.4.3

def sum_mul(n, m):
    if (n <= 0) or (m <= 0):
        return "INVALID"
    else:
        x = m // n      # 小於m的倍數數量
        maxn = x * n    # 最大的倍數
        
        # 最大倍數不可大於等於m
        if maxn == m:
            x -= 1
            maxn = x * n
            
        # 總和 = (首項 + 末項) * 項數 / 2
        return (n + maxn) * x / 2
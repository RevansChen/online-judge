class Solution(object):
    def reverse(self, x):
        MIN_INT32_VALUE = -(2 ** 31)
        MAX_INT32_VALUE = 2 ** 31 - 1
        
        # 去除符號
        x, sign = abs(x), x < 0
        
        # 數字顛倒
        revx = 0
        while x:
            x, revx = x // 10, revx * 10 + x % 10
        
        # 將符號補上
        if sign:
            revx = -revx
        
        # 溢位判斷
        if MIN_INT32_VALUE <= revx <= MAX_INT32_VALUE:
            return revx
        return 0
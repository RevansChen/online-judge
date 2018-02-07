import re

class Solution(object):
    def myAtoi(self, str):
        MIN_INT32_VALUE = -(2 ** 31)
        MAX_INT32_VALUE = 2 ** 31 - 1
        
        # 使用正則表達式判斷
        #     開頭是否為符號，最多一個
        #     後面接著一個以上的連續數字
        r = re.compile('^[-+]?[0-9]+')
        result = r.match(str.strip())
        if result:
            rt = int(result.group())
            # 範圍限制
            return min(max(rt, MIN_INT32_VALUE), MAX_INT32_VALUE)
        return 0

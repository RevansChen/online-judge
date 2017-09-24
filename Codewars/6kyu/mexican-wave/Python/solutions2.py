# Python - 3.4.3

def wave(str):
    result = []
    
    # 逐一掃描str每一個字元
    for i in range(len(str)):
        char = str[i]
        
        # 只對英文字母做處理
        if char.isalpha():
            front = str[:i]     # 前半部的字串
            char = char.upper() # 目前選到的字元要變大寫
            back = str[i+1:]    # 後半部的字串
            
            result.append(front + char + back)
            
    return result

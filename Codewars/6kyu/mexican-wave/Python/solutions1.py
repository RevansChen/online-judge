# Python - 3.4.3

def wave(str):
    # 逐一掃描str每一個字元，但只對英文字母做處理
    #
    # str[:i]     前半部的字串
    # str[i]      目前選到的字元
    # str[i+1:]   後半部的字串
    #
    # 當str = "codewars"且i = 3時
    #     str[:i]   => "cod"
    #     str[i]    => "e"
    #     str[i+1:] => "wars"
    return [ str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha() ]

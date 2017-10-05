# Python - 2.7.6

def correct_tail(body, tail):
    # 當tail長度大於body時, 傳回False
    # 當body尾端不為tail時, 傳回False
    return body.endswith(tail)
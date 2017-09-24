# Python - 3.4.3

def check_the_bucket(bucket):
    # 逐一檢查bucket內是否有 'gold', 有則傳回True
    for e in bucket:
        if e == 'gold':
            return True
    
    # 若都沒有則傳回False
    return False
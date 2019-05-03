# Python - 3.6.0

def contain_all_rots(strng, arr):
    if strng:
        for i in range(len(strng)):
            if not (strng[-i:] + strng[:-i]) in arr:
                return False
    return True

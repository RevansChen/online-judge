# Python - 3.6.0

def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False

# Python - 2.7.6

def my_first_kata(a, b):
    if (type(a) != int) or (type(b) != int):
        return False
    else:
        return a % b + b % a

# coding: utf-8
# Python3
def firstDuplicate(a):
    numbers = {}
    for index, number in enumerate(a):
        if number in numbers:
            return number
        else:
            numbers[number] = index
    return -1

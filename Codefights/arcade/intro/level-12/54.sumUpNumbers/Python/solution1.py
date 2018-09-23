# Python3

import re

def sumUpNumbers(inputString):
    return sum(map(int, re.findall(r'\d+', inputString)))

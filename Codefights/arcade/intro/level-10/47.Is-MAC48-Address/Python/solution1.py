# Python3

import re

def isMAC48Address(inputString):
    return re.match(r'^[0-9A-F]{2}(-[0-9A-F]{2}){5}$', inputString) != None

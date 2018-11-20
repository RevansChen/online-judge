# Python - 3.4.3

import re

def ipv4_address(address):
    return re.fullmatch(r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)$', address) != None

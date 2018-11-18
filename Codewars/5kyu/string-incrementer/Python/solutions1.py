# Python - 3.6.0

import re

def increment_string(s):
    string, num, n = '', '', 0
    if s:
        string, num = [*re.match(r'^(.*?)(\d*)$', s).groups()]
        n = int(num) if num else 0
    return string + str(n + 1).rjust(len(num), '0')

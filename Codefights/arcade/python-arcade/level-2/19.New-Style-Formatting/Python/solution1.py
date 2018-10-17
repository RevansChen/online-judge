# Python3

import re
def newStyleFormatting(s):
    return '%'.join(re.sub(r'%\w', '{}', x) for x in s.split('%%'))

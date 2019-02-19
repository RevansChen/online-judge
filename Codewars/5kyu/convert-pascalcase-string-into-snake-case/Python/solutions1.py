# Python - 3.6.0

import re

to_underscore = lambda string: '_'.join(map(lambda s: s.lower(), re.findall(r'[A-Z][^A-Z]*', str(string)))) or str(string)

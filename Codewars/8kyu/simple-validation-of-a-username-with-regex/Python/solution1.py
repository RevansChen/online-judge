# Python - 3.6.0

import re
validate_usr = lambda username: re.match('^[a-z0-9_]{4,16}$', username) is not None

# Python - 3.6.0

import re

validPhoneNumber = lambda phoneNumber: re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phoneNumber) != None

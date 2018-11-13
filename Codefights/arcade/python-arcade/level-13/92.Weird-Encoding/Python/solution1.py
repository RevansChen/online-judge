# Python3

import base64

def weirdEncoding(encoding, message):
    return base64.b64decode(message, encoding).decode()

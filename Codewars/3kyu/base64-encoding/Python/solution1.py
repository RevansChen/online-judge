# Python - 2.7.6

from base64 import b64encode, b64decode
from math import ceil

padChar = '='
def to_base_64(string):
    return b64encode(string).rstrip(padChar)

def from_base_64(string):
    b64Length = int(ceil(len(string) / 4.0)) * 4
    return b64decode(string.ljust(b64Length, padChar))

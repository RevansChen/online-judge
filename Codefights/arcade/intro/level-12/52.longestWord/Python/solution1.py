# Python3

import re

def longestWord(text):
    words = re.findall(r'[a-zA-Z]+', text)
    maxLen = max(len(word) for word in words)
    return [*filter(lambda word: len(word) == maxLen, words)][0]

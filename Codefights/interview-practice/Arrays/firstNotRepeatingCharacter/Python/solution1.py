# Python3

def firstNotRepeatingCharacter(s):
    characters = {}
    for ch in s:
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    notRepeatingCharacters = [ k for k, v in characters.items() if v == 1]
    if notRepeatingCharacters:
        return s[min(s.index(ch) for ch in notRepeatingCharacters)]
    else:
        return '_'

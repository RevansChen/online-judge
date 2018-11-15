# Python3

def areFollowingPatterns(strings, patterns):
    for i in range(len(strings)):
        for j in range(len(strings)):
            if i != j and ((strings[i] == strings[j] and patterns[i] != patterns[j]) or (strings[i] != strings[j] and patterns[i] == patterns[j])):
                return False
    return True

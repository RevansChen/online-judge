# Python - 3.6.0

is_opposite = lambda s1, s2: bool(s1 and s2) and (len(s1) == len(s2)) and all([s1[i] != s2[i] for i in range(len(s1))])

def almostIncreasingSequence(seq):
    groups = []
    startIndex = 0
    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            if len(groups) == 2:
                return False
            groups.append((startIndex, i))
            startIndex = i
    groups.append((startIndex, len(seq)))

    if len(groups) == 1:
        return True
    if len(groups) > 2:
        return False

    group1Length = groups[0][1] - groups[0][0]
    group2Length = groups[1][1] - groups[1][0]
    if (group1Length == 1) or (group2Length == 1):
        return True
    
    group1Tail1, group1Tail2 = seq[groups[0][1] - 1], seq[groups[0][1] - 2]
    group1Head1, group1Head2 = seq[groups[1][0]], seq[groups[1][0] + 1]
    return (group1Head1 > group1Tail2) or (group1Head2 > group1Tail1)

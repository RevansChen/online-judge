# Python3

def fileNaming(names):
    nameMap = {}
    output = []
    for name in names:
        newName = name
        if newName in output:
            num = nameMap.get(newName, 0)
            while True:
                nm = '%s(%d)' % (newName, num)
                num += 1
                nameMap[newName] = num
                if not nm in output:
                    newName = nm
                    break

        output.append(newName)
        nameMap[newName] = 1

    return output

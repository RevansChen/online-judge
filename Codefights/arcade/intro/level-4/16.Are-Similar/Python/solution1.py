# Python3

def areSimilar(a, b):
    if a == b:
        return True
    
    index = []
    for i in range(len(a)):
        if a[i] != b[i]:
            index.append(i)
        if len(index) > 2:
            return False
    return (len(index) == 2) and (a[index[0]] == b[index[1]]) and (a[index[1]] == b[index[0]])

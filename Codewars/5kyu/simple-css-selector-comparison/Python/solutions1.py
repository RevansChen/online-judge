# Python - 2.7.6

def calcWeight(ss):
    for ch in ['.', '#']:
        ss = ss.replace(ch, ' ' + ch)
    ss = ss.strip(' ')

    id, cs, tag = 0, 0, 0
    if ss != '*':
        for selector in ss.split(' '):
            if len(selector):
                if selector.startswith('.'):
                    cs += 1
                elif selector.startswith('#'):
                    id += 1
                else:
                    tag += 1
    return (id, cs, tag)

def compare(a, b):
    wa = calcWeight(a)
    wb = calcWeight(b)
    return a if wa > wb else b

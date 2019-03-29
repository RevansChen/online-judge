# Python - 3.6.0

def ranking(people):
    rank = sorted(sorted(people, key = lambda e: e['name']), key = lambda e: e['points'], reverse = True)
    
    points = ''
    position, offset = 0, 0
    for e in rank:
        if points != e['points']:
            position += 1 + offset
            points = e['points']
            offset = 0
        else:
            offset += 1
        e['position'] = position

    return rank

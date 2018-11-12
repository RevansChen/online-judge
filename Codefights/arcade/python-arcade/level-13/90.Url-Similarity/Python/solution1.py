# Python3

import re

def urlSimilarity(url1, url2):
    pattern = r'(\w+):\/\/([\w.]+)((\/\w+)*)((\?\w+=\w+)*(&\w+=\w+)*)'
    protocol1, address1, path1, _, query1, _, _ = re.match(pattern, url1).groups()
    protocol2, address2, path2, _, query2, _, _ = re.match(pattern, url2).groups()

    score = 0
    if protocol1 == protocol2:
        score += 5

    if address1 == address2:
        score += 10

    if path1.startswith('/'):
        path1 = path1[1:]
    if path2.startswith('/'):
        path2 = path2[1:]
    if path1 and path2:
        p1s = path1.split('/')
        p2s = path2.split('/')
        for i in range(min(len(p1s), len(p2s))):
            if p1s[i] == p2s[i]:
                score += 1
            else:
                break

    if query1.startswith('?'):
        query1 = query1[1:]
    if query2.startswith('?'):
        query2 = query2[1:]
    if query1 and query2:
        q1s = { k: v for k, v in map(lambda x: x.split('='), query1.split('&')) }
        q2s = { k: v for k, v in map(lambda x: x.split('='), query2.split('&')) }
        qset = set(q1s.keys()) & set(q2s.keys())
        score += len(qset)
        for q in qset:
            if q1s[q] == q2s[q]:
                score += 1
    return score

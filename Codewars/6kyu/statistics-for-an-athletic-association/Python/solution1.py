# Python - 3.6.0

import re

toInt = lambda s: int(s) if s else 0
formatTime = lambda sec: f'{sec // 3600:#02d}|{(sec // 60) % 60:#02d}|{sec % 60:#02d}'

def stat(strg):
    if re.match(r'\d*\|\d*\|\d*', strg) == None:
        return ''

    times = []
    avg = 0
    team = strg.split(', ')
    for t in team:
        sp = t.split('|')
        sec = toInt(sp[0]) * 3600 + toInt(sp[1]) * 60 + toInt(sp[2])
        avg += sec
        times.append(sec)
    times.sort()

    avg = int(avg / len(team))

    r = times[-1] - times[0]

    m = int(len(times) / 2)
    mid = times[m]
    if not (len(times) & 1):
        mid = int((mid + times[m - 1]) / 2)

    return ' '.join([
        f'Range: {formatTime(r)}',
        f'Average: {formatTime(avg)}',
        f'Median: {formatTime(mid)}'
    ])

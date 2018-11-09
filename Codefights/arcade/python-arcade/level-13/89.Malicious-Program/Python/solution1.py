# Python3

from time import strptime, strftime
from calendar import monthrange

def maliciousProgram(curDate, changes):
    cur = strptime(curDate, '%d %b %Y %H:%M:%S')
    mday = cur.tm_mday + changes[0]
    mon = cur.tm_mon + changes[1]
    year = cur.tm_year + changes[2]
    hour = cur.tm_hour + changes[3]
    min = cur.tm_min + changes[4]
    sec = cur.tm_sec + changes[5]

    conditions = [
        1 <= mday <= 31,
        1 <= mon <= 12,
        0 <= year,
        0 <= hour <= 23,
        0 <= min <= 59,
        0 <= sec <= 59
    ]

    if all(conditions) and mday <= monthrange(year, mon)[1]:
        return strftime('%d %b %Y %H:%M:%S', (year, mon, mday, hour, min, sec, 0, 0, 0))
    return curDate

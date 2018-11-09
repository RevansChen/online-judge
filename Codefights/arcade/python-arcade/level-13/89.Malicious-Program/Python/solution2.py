# Python3

from datetime import datetime

def maliciousProgram(curDate, changes):
    format = '%d %b %Y %H:%M:%S'
    cur = datetime.strptime(curDate, format)

    try:
        return datetime(
            cur.year + changes[2],
            cur.month + changes[1],
            cur.day + changes[0],
            cur.hour + changes[3],
            cur.minute + changes[4],
            cur.second + changes[5]
        ).strftime(format)
    except:
        return curDate

# Python3

def validTime(time):
    hour, minute = map(int, time.split(':'))
    return hour < 24 and minute < 60

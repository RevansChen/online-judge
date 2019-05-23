# Python - 2.7.6

def day_and_time(mins):
    MAX_MINUTES = 7 * 24 * 60
    mins = mins % MAX_MINUTES
    if mins < 0:
        mins += MAX_MINUTES
    hrs, mins = mins // 60, mins % 60
    weeks, hrs = hrs // 24, hrs % 24
    w = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return '{} {:0>2d}:{:0>2d}'.format(w[weeks], hrs, mins)

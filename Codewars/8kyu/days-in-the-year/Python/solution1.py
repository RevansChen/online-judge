# Python - 2.7.6

def year_days(year):
    leap = ((year % 4) == 0) and (not ((year % 100) == 0) or ((year % 400) == 0))
    return '%d has %d days' % (year, 366 if leap else 365)

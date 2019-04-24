# Python - 3.6.0

unlucky_days = lambda year: sum(__import__('datetime').date(year, month, 13).weekday() == 4 for month in range(1, 13))

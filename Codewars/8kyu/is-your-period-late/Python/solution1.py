# Python - 3.6.0

def period_is_late(last, today, cycle_length):
    delta = today - last
    return delta.days > cycle_length

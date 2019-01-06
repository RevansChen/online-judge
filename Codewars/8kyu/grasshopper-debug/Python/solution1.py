# Python - 2.7.6

def weather_info(fahrenheit):
    celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
    return '%s is%s freezing temperature' % (str(celsius), ' above' if celsius >= 0 else '')

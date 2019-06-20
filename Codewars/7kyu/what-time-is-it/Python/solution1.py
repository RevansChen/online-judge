# Python - 3.6.0

get_military_time = lambda t: f'{(int(t[:2]) % 12 + (t[-2] == "P") * 12):02d}{t[2:8]}'

# Python - 2.7.6

ip_to_int32 = lambda ip: reduce(lambda x, y: x * 256 + y, map(int, ip.split('.')))

# Python - 3.6.0

pass_hash = lambda string: (lambda m: m.update(bytes(string, encoding = 'ascii')) or m.hexdigest())(__import__('hashlib').md5(b''))

# Python - 3.6.0

encrypt_this = lambda text: ' '.join(f'{ord(s[0])}{s[1:] if len(s) < 3 else (s[-1] + s[2:-1] + s[1])}' for s in text.split(' ') if s)

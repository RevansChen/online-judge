# Python - 3.6.0

expanded_form = lambda num: ' + '.join([s + '0' * (len(str(num)) - i - 1) for i, s in enumerate(str(num)) if s != '0'])

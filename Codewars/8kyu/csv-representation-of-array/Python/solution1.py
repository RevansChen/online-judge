# Python - 3.6.0

toCsvText = lambda array: '\n'.join(map(lambda line: ','.join(map(lambda e: str(e), line)), array))

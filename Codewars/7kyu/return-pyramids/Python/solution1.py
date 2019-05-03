# Python - 3.6.0

pyramid = lambda n: '\n'.join(f'{" " * (n - i - 1)}/{("  " if i != (n - 1) else "__") * (i)}\\' for i in range(n)) + '\n'

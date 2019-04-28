# Python - 3.6.0

nb_dig = lambda n, d: sum(str(i * i).count(str(d)) for i in range(n + 1))

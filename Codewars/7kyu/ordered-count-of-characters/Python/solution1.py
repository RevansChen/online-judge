# Python - 3.6.0

ordered_count = lambda input: sorted([(c, input.count(c)) for c in set(input)], key = lambda x: input.index(x[0]))

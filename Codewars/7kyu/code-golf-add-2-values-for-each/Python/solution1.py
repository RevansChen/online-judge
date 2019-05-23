# Python - 3.6.0

make_new_list = lambda l: [*map(sum, zip(l, l[1:]))]

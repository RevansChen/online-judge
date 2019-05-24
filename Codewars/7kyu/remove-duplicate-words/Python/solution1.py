# Python - 3.6.0

remove_duplicate_words = lambda s: (lambda words = s.split(' '): ' '.join(sorted(set(words), key = words.index)))()

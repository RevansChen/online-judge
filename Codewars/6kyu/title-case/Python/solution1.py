# Python - 3.6.0

title_case = lambda title, minor_words = '': ' '.join([e.lower() if i != 0 and (e in minor_words.lower().split(' ')) else e.capitalize() for i, e in enumerate(title.lower().split(' '))])

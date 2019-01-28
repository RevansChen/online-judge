# Python - 3.6.0

reverse = lambda st: ' '.join([*filter(lambda e: e, st.split(' '))][::-1]).strip()

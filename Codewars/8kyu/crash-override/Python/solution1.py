# Python - 3.6.0

def alias_gen(f_name, l_name):
    f = f_name[0].upper()
    l = l_name[0].upper()
    if (f in FIRST_NAME) and (l in SURNAME):
        return f'{FIRST_NAME[f]} {SURNAME[l]}'

    return 'Your name must start with a letter from A - Z.'

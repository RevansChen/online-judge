# Python - 3.6.0

def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    if diff > 0:
        return f'You are {diff} year{"s" if diff > 1 else ""} old.'
    elif diff == 0:
        return 'You were born this very year!'
    else:
        diff = -diff
        return f'You will be born in {diff} year{"s" if diff > 1 else ""}.'

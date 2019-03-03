# Python - 3.6.0

def solution(a, b):
    units = {
        'g': 1e-3,
        'mg': 1e-6,
        'μg': 1e-9,
        'lb': 0.453592,
        'cm': 1e-2,
        'mm': 1e-3,
        'μm': 1e-6,
        'ft': 0.3048
    }
    m1, m2, r = [*map(lambda e: e[0] * units.get(e[1], 1), zip(a, b))]
    return 6.67e-11 * m1 * m2 / (r ** 2)

# Python - 3.6.0

def wallpaper(l, w, h):
    return {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'
    }.get(int(__import__('math').ceil((2 * (l + w) * h if l and w and h else 0) * 1.15 / 5.2)), 'zero')


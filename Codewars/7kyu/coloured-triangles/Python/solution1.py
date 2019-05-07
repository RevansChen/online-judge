# Python - 3.6.0

def triangle(row):
    d = {
        'RR': 'R', 'GG': 'G', 'BB': 'B',
        'RG': 'B', 'GR': 'B',
        'GB': 'R', 'BG': 'R',
        'RB': 'G', 'BR': 'G'
    }
    while len(row) > 1:
        row = ''.join(d[row[i:i + 2]] for i in range(len(row) - 1))
    return row

# Python - 3.6.0

get_issuer = lambda number: (
    lambda n = str(number), table = {
        'AMEX': (['34', '37'], [15]),
        'Discover': (['6011'], [16]),
        'Mastercard': (['51', '52', '53', '54', '55'], [16]),
        'VISA': (['4'], [13, 16])
    }: {
        any(map(n.startswith, v[0])) and any(map(lambda x: len(n) == x, v[1])): k for k, v in table.items()
    }.get(True, 'Unknown')
)()

# Python - 3.6.0

to_leet_speak = lambda s: s.translate(
    str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '@8(D3F6#!JK1MN0PQR$7UVWXY2'
    )
)

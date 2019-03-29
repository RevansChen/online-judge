# Python - 3.6.0

points = lambda games: sum(map(lambda r: 3 if r[0] > r[1] else 0 if r[0] < r[1] else 1, map(lambda game: [*map(int, game.split(':'))], games)))

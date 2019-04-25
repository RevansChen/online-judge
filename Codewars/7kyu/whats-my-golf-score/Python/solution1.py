# Python - 3.6.0

golf_score_calculator = lambda par_string, score_string: sum(int(s) - int(par_string[i]) for i, s in enumerate(score_string))

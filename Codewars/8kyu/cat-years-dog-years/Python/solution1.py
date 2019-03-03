# Python - 3.6.0

human_years_cat_years_dog_years = lambda human_years: [
    human_years,
    15 + (9 if human_years > 1 else 0) + max((human_years - 2) * 4, 0),
    15 + (9 if human_years > 1 else 0) + max((human_years - 2) * 5, 0)
]

# Python - 2.7.6

from math import ceil
ratings = {
    'terrible': 0,
    'poor': 0.05,
    'good': 0.1,
    'great': 0.15,
    'excellent': 0.2,
}
calculate_tip = lambda amount, rating: ceil(ratings[rating.lower()] * amount) if rating.lower() in ratings else 'Rating not recognised'

# Python - 3.6.0

import math

EPSILON = 0.01

def circular_area(x, y):
    if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25:
        return True
    return False

def full_shape(x, y):
    if 0 < x < 1 and 0 < y < 1:
        return True
    return False

Test.expect(abs(area_of_the_shape(circular_area) - 0.25 * math.pi) <= EPSILON, 'On testing a circular shape bounded by the area')
Test.expect(abs(area_of_the_shape(full_shape) - 1) <= EPSILON, 'On testing the whole area')

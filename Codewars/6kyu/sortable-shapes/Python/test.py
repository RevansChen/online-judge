# Python - 3.4.3

from random import shuffle

test.describe('Base class checks')

test.assert_equals(all(issubclass(x, Shape) for x in (Triangle, Circle, Rectangle, CustomShape, Square)), True)

test.describe('Shapes are sortable on are')

expected = []

area = 1.1234
expected.append(CustomShape(area))

side = 1.1234
expected.append(Square(side))

radius = 1.1234
expected.append(Circle(radius))

triangleBase = 5
height = 2
expected.append(Triangle(triangleBase, height))

height = 3
triangleBase = 4
expected.append(Triangle(triangleBase, height))

width = 4
expected.append(Rectangle(width, height))

area = 16.1
expected.append(CustomShape(area))

test.it('Base class check')
test.assert_equals(all(issubclass(x, Shape) for x in (Triangle, Circle, Rectangle, CustomShape, Square)), True)

# create a copy of expected
actual = expected[:]

# in-place shuffle (check: https://docs.python.org/3.6/library/random.html?highlight=shuffle#random.shuffle)
shuffle(actual)
actual.sort()

test.assert_equals(actual, expected)

# Python - 3.4.3

import math

class Shape:
    def __init__(self, area):
        self.area = area
    
    def __lt__(self, other):
        return self.area < other.area
    
class CustomShape(Shape):
    def __init__(self, area):
        super(CustomShape, self).__init__(area)
        
class Square(Shape):
    def __init__(self, side):
        super(Square, self).__init__(side ** 2)

class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__(math.pi * radius ** 2)

class Triangle(Shape):
    def __init__(self, triangleBase, height):
        super(Triangle, self).__init__(triangleBase * height / 2.0)

class Rectangle(Shape):
    def __init__(self, width, height):
        super(Rectangle, self).__init__(width * height)

# Python - 2.7.6

class Cat(Animal):
    def __init__(self, name):
        self.__name = name
    def speak(self):
        return '%s meows.' % self.__name

# Python - 3.6.0

class Cube:
    def __init__(self, arg = 0):
        self.__side = arg

    def get_side(self):
        '''Return the side of the Cube'''
        return self.__side

    def set_side(self, new_side):
        '''Set the value of the Cube's side.'''
        self.__side = abs(new_side)

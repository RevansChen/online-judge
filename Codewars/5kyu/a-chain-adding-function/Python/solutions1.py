# Python - 3.4.3

class Integer(int):
    def __call__(self, *args, **kwargs):
        return Integer(self + args[0])
        
def add(val):
    return Integer(val)
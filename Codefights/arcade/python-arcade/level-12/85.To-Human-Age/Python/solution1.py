# Python3

# 有限制修改區域
class Mammal(object):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'{self.toHuman()} y.o. in human age'

    def toHuman(self):
        return self.age

class Cat(Mammal):
    def toHuman(self):
        if self.age == 0:
            return 0
        elif self.age < 3:
            return 25 // (3 - self.age)
        else:
            return 25 + 4 * (self.age - 2)

class Dog(Mammal):
    def toHuman(self):
        if self.age == 0:
            return 0
        elif self.age == 1:
            return 15
        elif self.age == 2:
            return 24
        else:
            return 24 + (self.age - 2) * 4

class Human(Mammal):
    pass


def toHumanAge(members):
    species = {
        'cat': Cat,
        'dog': Dog,
        'human': Human
    }
    res = []
    for spec, age in members:
        res.append(str(species[spec](int(age))))
    return res

# Python - 3.6.0

class Vector:
    def __init__(self, vec):
        self.__vec = vec

    def __str__(self):
        return f'({",".join(map(str, self.__vec))})'

    def __getitem__(self, index):
        return self.__vec[index]

    def __calc(self, v, func):
        if self.__differentLength(v):
            raise Exception('')
        return Vector([func(self.__vec[i], e) for i, e in enumerate(v)])

    def __differentLength(self, v):
        return len(self.__vec) != len(v)

    def __len__(self):
        return len(self.__vec)

    def add(self, v):
        return self.__calc(v, lambda a, b: a + b)

    def subtract(self, v):
        return self.__calc(v, lambda a, b: a - b)

    def dot(self, v):
        return sum(self.__calc(v, lambda a, b: a * b))

    def norm(self):
        return sum([i * i for i in self.__vec]) ** 0.5

    def equals(self, v):
        if len(self.__vec) != len(v):
            return False
        for i, e in enumerate(self.__vec):
            if e != v[i]:
                return False
        return True

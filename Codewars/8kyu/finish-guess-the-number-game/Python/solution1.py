# Python - 2.7.6

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives <= 0:
            raise Error('Omae wa mo shindeiru')
        if n != self.number:
            self.lives -= 1
        return n == self.number

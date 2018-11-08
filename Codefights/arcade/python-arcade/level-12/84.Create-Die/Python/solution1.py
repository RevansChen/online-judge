# Python3

# 有限制修改區域
import random

def createDie(seed, n):
    class Die(object):
        def __new__(self, seed, n):
            random.seed(seed)
            return int(random.random() * n) + 1

    class Game(object):
        die = Die(seed, n)

    return Game.die

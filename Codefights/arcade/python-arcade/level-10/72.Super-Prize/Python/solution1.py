# Python3

# 有限制修改區域
class Prizes(object):
    def __init__(self, purchases, n, d):
        self.i = n - 1
        self.purchases = purchases
        self.n = n
        self.d = d

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.purchases):
            currIndex = self.i
            self.i += self.n
            if (self.purchases[currIndex] % self.d) == 0:
                return currIndex + 1
        raise StopIteration

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

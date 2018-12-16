# Python - 3.6.0

class User:
    RANK = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.progress = 0
        self.rank = User.RANK[0]

    def inc_progress(self, activityRank):
        if not activityRank in User.RANK:
            raise ValueError()

        if self.rank == User.RANK[-1]:
            return

        d = User.RANK.index(activityRank) - User.RANK.index(self.rank)
        p = 1 if d < 0 else (3 if d == 0 else (10 * d * d))
        self.progress += p

        if self.progress >= 100:
            r, self.progress = divmod(self.progress, 100)
            i = User.RANK.index(self.rank)
            self.rank = User.RANK[min(i + r, len(User.RANK) - 1)]
            if self.rank == User.RANK[-1]:
                self.progress = 0

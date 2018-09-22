# Python3

def electionsWinners(votes, k):
    maxCount = votes.count(max(votes))
    if k == 0 and maxCount == 1:
        return 1
    maxVote = max(votes)
    return sum(1 for vote in votes if (vote + k) > maxVote)

# Python3

def containsCloseNums(nums, k):
    ns = {}
    for i, n in enumerate(nums):
        if (n in ns) and (abs(ns[n] - i) <= k):
            return True
        ns[n] = i
    return False

# Python - 3.6.0

def solve(s, k):
    count = 0
    nums = s.split(' ')
    for i, ni in enumerate(nums):
        for j, nj in enumerate(nums):
            if (i != j) and (int(ni + nj) % k == 0):
                count += 1
    return count

# Python - 2.7.6

def iq_test(numbers):
    nums = map(lambda s: int(s) % 2, numbers.split(' '))
    total = sum(nums)
    target = 1 if (total == 1) else 0
    return nums.index(target) + 1

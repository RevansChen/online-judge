# Python - 2.7.6

def narcissistic(value):
    v, nums = value, []
    while v > 0:
        nums.append(v % 10)
        v = v // 10
    return sum(map(lambda num: num ** len(nums), nums)) == value

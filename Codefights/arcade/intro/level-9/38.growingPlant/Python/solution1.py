# Python3

from math import ceil
def growingPlant(upSpeed, downSpeed, desiredHeight):
    return max(1, ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed)) + 1)

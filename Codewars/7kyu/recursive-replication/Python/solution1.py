# Python - 3.6.0

@countcalls
def replicate(times, number):
    return [number] + replicate(times - 1, number) if times > 0 else []

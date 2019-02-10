# Python - 3.6.0

def sqInRect(wdth, lng):
    if lng == wdth:
        return None

    wdth, lng = max(wdth, lng), min(wdth, lng)

    results = []
    while (wdth > 0) and (lng > 0):
        results.append(lng)
        wdth, lng = max(lng, wdth - lng), min(lng, wdth - lng)

    return results

# Python - 3.6.0

def catch_sign_change(lst):
    count = 0
    if lst:
        last = lst[0] < 0
        for e in lst[1:]:
            curr = e < 0
            if curr != last:
                count += 1
            last = curr
    return count

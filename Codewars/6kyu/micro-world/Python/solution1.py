# Python - 3.6.0

def micro_world(bacteria, k):
    mark = set()
    bacteriaSet = set(bacteria)
    for i, bi in enumerate(bacteriaSet):
        for j, bj in enumerate(bacteriaSet):
            if (i != j) and (not bj in mark) and (bj < bi <= (bj + k)):
                mark.add(bj)
    return len([*filter(lambda b: not b in mark, bacteria)])

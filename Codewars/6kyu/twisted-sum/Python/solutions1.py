# Python - 3.4.3

def compute_sum(n):
    total = { i: 0 for i in range(1, 10) }
    d = 1
    while d <= n:
        ab, c = divmod(n, d)
        a, b = divmod(ab, 10)

        for i in range(1, 10):
            count = 0
            if i < b:
                count = (a + 1) * d
            elif i == b:
                count = a * d + c + 1
            else:
                count = a * d
            total[i] += count

        d *= 10

    return sum((i * count) for i, count in total.items())

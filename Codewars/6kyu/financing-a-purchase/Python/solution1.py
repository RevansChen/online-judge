# Python - 3.6.0

def amort(rate, bal, term, num_payments):
    r = rate / 1200
    n = r * bal
    d = 1 - (1 + r) ** (-term)
    c = n / d
    princ = c - n
    for i in range(num_payments - 1):
        bal -= princ
        n = r * bal
        princ = c - n
    bal -= princ
    return f'num_payment {num_payments} c {round(c)} princ {round(princ)} int {round(n)} balance {round(bal)}'

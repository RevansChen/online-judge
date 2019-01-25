# Python - 3.6.0

from functools import reduce
distinct = lambda seq: reduce(lambda ls, e: ls + ([] if e in ls else [e]), seq, [])

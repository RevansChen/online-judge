# Python - 3.6.0

def movie(card, ticket, perc):
    from math import ceil
    n = 0
    systemA, systemB = 0, card
    t = ticket
    while ceil(systemB) >= systemA:
        n += 1
        t *= perc
        systemA += ticket
        systemB += t
    return n

# Python - 2.7.6

def balance_statement(lst):
    import re
    mistakes = []
    buy, sell = 0.0, 0.0
    if lst:
        for i, order in enumerate(re.split(r',\s?', lst)):
            m = re.match(r'^[\w\.]+ (\w+) (\w*\.\w+) (\w)$', order)
            if m:
                price = float(m.group(1)) * float(m.group(2))
                if m.group(3) == 'B':
                    buy += price
                elif m.group(3) == 'S':
                    sell += price
                else:
                    mistakes.append(order)
            else:
                mistakes.append(order)
    
    total = 'Buy: %d Sell: %d' % (round(buy, 0), round(sell, 0))
    if mistakes:
        return '%s; Badly formed %d: %s' % (total, len(mistakes), ' ;'.join(mistakes + ['']))
    return total

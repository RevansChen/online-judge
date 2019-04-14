# Python - 2.7.6

eval_object = lambda v: {
    '+':  v['a'] +  v['b'],
    '-':  v['a'] -  v['b'],
    '/':  v['a'] /  v['b'],
    '*':  v['a'] *  v['b'],
    '%':  v['a'] %  v['b'],
    '**': v['a'] ** v['b']
}.get(v['operation'], 0)

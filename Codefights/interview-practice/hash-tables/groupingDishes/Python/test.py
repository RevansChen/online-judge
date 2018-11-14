# Python3

from solution1 import groupingDishes as f

qa = [
    ([['Salad','Tomato','Cucumber','Salad','Sauce'],
      ['Pizza','Tomato','Sausage','Sauce','Dough'],
      ['Quesadilla','Chicken','Cheese','Sauce'],
      ['Sandwich','Salad','Bread','Tomato','Cheese']],
     [['Cheese','Quesadilla','Sandwich'],
      ['Salad','Salad','Sandwich'],
      ['Sauce','Pizza','Quesadilla','Salad'],
      ['Tomato','Pizza','Salad','Sandwich']]),
    ([['Pasta','Tomato Sauce','Onions','Garlic'],
      ['Chicken Curry','Chicken','Curry Sauce'],
      ['Fried Rice','Rice','Onions','Nuts'],
      ['Salad','Spinach','Nuts'],
      ['Sandwich','Cheese','Bread'],
      ['Quesadilla','Chicken','Cheese']],
     [['Cheese','Quesadilla','Sandwich'],
      ['Chicken','Chicken Curry','Quesadilla'],
      ['Nuts','Fried Rice','Salad'],
      ['Onions','Fried Rice','Pasta']]),
    ([['Pasta','Tomato Sauce','Onions','Garlic'],
      ['Chicken Curry','Chicken','Curry Sauce'],
      ['Fried Rice','Rice','Onion','Nuts'],
      ['Salad','Spinach','Nut'],
      ['Sandwich','Cheese','Bread'],
      ['Quesadilla','Chickens','Cheeseeee']],
     []),
    ([['First','a','b','c','d','e','f','g','h','i'],
      ['Second','i','h','g','f','e','x','c','b','a']],
     [['a','First','Second'],
      ['b','First','Second'],
      ['c','First','Second'],
      ['e','First','Second'],
      ['f','First','Second'],
      ['g','First','Second'],
      ['h','First','Second'],
      ['i','First','Second']])
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = f(*q)
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()

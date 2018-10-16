# Python3

from solution1 import feedbackReview as f

qa = [
    ('This is an example feedback', 8,
     ['This is',
      'an',
      'example',
      'feedback']),
    ('This is an example feedback', 40,
     ['This is an example feedback']),
    ('', 10,
     []),
    ('Dude, do you even review these feedbacks?', 16,
     ['Dude, do you',
      'even review',
      'these feedbacks?']),
    ("I'm not sure how your service is supposed to work, is there some readme or something?", 12,
     ["I'm not sure",
      'how your',
      'service is',
      'supposed to',
      'work, is',
      'there some',
      'readme or',
      'something?'])
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

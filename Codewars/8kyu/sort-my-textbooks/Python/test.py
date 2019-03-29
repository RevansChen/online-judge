# Python - 3.6.0

test.expect(sorter(['Algebra', 'History', 'Geometry', 'English']) == ['Algebra', 'English', 'Geometry', 'History'], 'Does not sort strings')
test.expect(sorter(['Algebra', 'history', 'Geometry', 'english']) == ['Algebra', 'english', 'Geometry', 'history'], 'Does not handle capitalization')
test.expect(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']) == ['$istory', '**english', 'Alg#bra', 'Geom^try'], 'Does not handle symbols')

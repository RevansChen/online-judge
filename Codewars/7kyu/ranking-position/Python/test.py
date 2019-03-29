# Python - 3.6.0

input_ = [
    { 'name': 'John', 'points': 100 },
    { 'name': 'Bob',  'points': 130 },
    { 'name': 'Mary', 'points': 120 },
    { 'name': 'Kate', 'points': 120 }
]
output = [
    { 'name': 'Bob',  'points': 130, 'position': 1 },
    { 'name': 'Kate', 'points': 120, 'position': 2 },
    { 'name': 'Mary', 'points': 120, 'position': 2 },
    { 'name': 'John', 'points': 100, 'position': 4 }
]
Test.assert_equals(ranking(input_), output)

input_ = [
    { 'name': 'Bob',  'points': 130 },
    { 'name': 'Mary', 'points': 120 },
    { 'name': 'John', 'points': 100 }
]
output = [
    { 'name': 'Bob',  'points': 130, 'position': 1 },
    { 'name': 'Mary', 'points': 120, 'position': 2 },
    { 'name': 'John', 'points': 100, 'position': 3 }
]
Test.assert_equals(ranking(input_), output)

input_ = [
    { 'name': 'Bob',  'points': 100 },
    { 'name': 'Mary', 'points': 100 },
    { 'name': 'John', 'points': 100 }
]
output = [
    { 'name': 'Bob',  'points': 100, 'position': 1 },
    { 'name': 'John', 'points': 100, 'position': 1 },
    { 'name': 'Mary', 'points': 100, 'position': 1 }
]
Test.assert_equals(ranking(input_), output)

input_ = [{ 'name': 'Joe', 'points': 100 }]
output = [{ 'name': 'Joe', 'points': 100, 'position': 1 }]
Test.assert_equals(ranking(input_), output)

Test.assert_equals(ranking([]), [])

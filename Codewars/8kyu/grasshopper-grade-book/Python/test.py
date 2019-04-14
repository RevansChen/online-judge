# Python - 3.6.0

test.describe('grade book')
test.it('should return an A')
test.assert_equals(get_grade(95, 90, 93), 'A', 'get_grade(95, 90, 93)')
test.assert_equals(get_grade(100, 85, 96), 'A', 'get_grade(100, 85, 96)')
test.assert_equals(get_grade(92, 93, 94), 'A', 'get_grade(92, 93, 94)')

test.it('should return a B')
test.assert_equals(get_grade(70, 70, 100), 'B', 'get_grade(70, 70, 100)')
test.assert_equals(get_grade(82, 85, 87), 'B', 'get_grade(82, 85, 87)')
test.assert_equals(get_grade(84, 79, 85), 'B', 'get_grade(84, 79, 85)')

test.it('should return a C')
test.assert_equals(get_grade(70, 70, 70), 'C', 'get_grade(70, 70, 70)')
test.assert_equals(get_grade(75, 70, 79), 'C', 'get_grade(75, 70, 79)')
test.assert_equals(get_grade(60, 82, 76), 'C', 'get_grade(60, 82, 76)')

test.it('should return a D')
test.assert_equals(get_grade(65, 70, 59), 'D', 'get_grade(65, 70, 59)')
test.assert_equals(get_grade(66, 62, 68), 'D', 'get_grade(66, 62, 68)')
test.assert_equals(get_grade(58, 62, 70), 'D', 'get_grade(58, 62, 70)')

test.it('should return an F')
test.assert_equals(get_grade(44, 55, 52), 'F', 'get_grade(44, 55, 52)')
test.assert_equals(get_grade(48, 55, 52), 'F', 'get_grade(48, 55, 52)')
test.assert_equals(get_grade(58, 59, 60), 'F', 'get_grade(58, 59, 60)')

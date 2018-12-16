# Python - 3.6.0

Test.expect(0 == bowling_score([0] * 20))
Test.expect(190 == bowling_score([9, 1] * 10 + [9]))
Test.expect(300 == bowling_score([10] * 12))
Test.expect(11 == bowling_score([
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    10, 1, 0
]))
Test.expect(12 == bowling_score([
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    0, 0,
    10,
    1, 0
]))


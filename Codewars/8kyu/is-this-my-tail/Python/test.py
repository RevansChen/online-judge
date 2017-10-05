# Python - 2.7.6

Test.describe("Basic tests")
Test.assert_equals(correct_tail("Fox", "x"), True)
Test.assert_equals(correct_tail("Fox", "ox"), True)
Test.assert_equals(correct_tail("Fox", "Fox"), True)
Test.assert_equals(correct_tail("Fox", "FFox"), False)
Test.assert_equals(correct_tail("Rhino", "o"), True)
Test.assert_equals(correct_tail("Meerkat", "t"), True)
Test.assert_equals(correct_tail("Emu", "t"), False)
Test.assert_equals(correct_tail("Badger", "s"), False)
Test.assert_equals(correct_tail("Giraffe", "d"), False)
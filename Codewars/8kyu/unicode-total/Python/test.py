# Python - 2.7.6

Test.describe("Basic tests")

Test.it("Should work with Single Letters")
Test.assert_equals(uni_total("a"), 97)
Test.assert_equals(uni_total("b"), 98)
Test.assert_equals(uni_total("c"), 99)

Test.it("no chars should return zero")
Test.assert_equals(uni_total(""), 0)

Test.it("should work with multiple letters")
Test.assert_equals(uni_total("aaa"), 291)
Test.assert_equals(uni_total("abc"), 294)

Test.it("should work with sentences and spaces")
Test.assert_equals(uni_total("Mary Had A Little Lamb"), 1873)
Test.assert_equals(uni_total("Mary had a little lamb"), 2001)
Test.assert_equals(uni_total("CodeWars rocks"), 1370)
Test.assert_equals(uni_total("And so does Strive"), 1661)
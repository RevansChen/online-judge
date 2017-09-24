# Python - 3.4.3

def _wrap(str, result):
    test.it("Should return: '[" + ", ".join(result) + "]'")
    test.assert_equals(wave(str), result)

# 無空白字元的字串
result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
_wrap("hello", result)

# 空字串
result = []
_wrap("", result)

# 含空白字元
result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
_wrap("two words", result)

result = [" Gap ", " gAp ", " gaP "]
_wrap(" gap ", result)

# Python - 2.7.6

def testAndPrint(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print "<pre style='display:inline'>Got '%s', expected '%s'</pre>" % (got, expected)
        test.expect(False)

test.describe('Example from description')
testAndPrint(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

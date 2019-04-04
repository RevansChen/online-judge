// JavaScript - Node v8.1.3

Test.expect(isReallyNaN(37) === false);
Test.expect(isReallyNaN('37') === false);
Test.expect(isReallyNaN(NaN) === true);
Test.expect(isReallyNaN(undefined) === false);

// JavaScript - Node v8.1.3

Test.assertEquals(SafeInteger(9007199254740992), false, 'Value returned should be false');
Test.assertEquals(SafeInteger(9007199254740990), true, 'Value returned should be true');

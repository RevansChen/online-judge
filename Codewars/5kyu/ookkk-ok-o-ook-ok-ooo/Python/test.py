# Python - 3.6.0

Test.assert_equals(okkOokOo('Ok, Ook, Ooo!'), 'H')
Test.assert_equals(okkOokOo('Okk, Ook, Ok!'), 'e')
Test.assert_equals(okkOokOo('Okk, Okk, Oo!'), 'l')
Test.assert_equals(okkOokOo('Okk, Okkkk!'), 'o')

Test.assert_equals(okkOokOo('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!'), 'Hello')
print('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!')
print(f'> {okkOokOo("Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!")}')


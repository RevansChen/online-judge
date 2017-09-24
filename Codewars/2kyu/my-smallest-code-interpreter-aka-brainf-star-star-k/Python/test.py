# Python - 2.7.6

# Echo until byte(255) encountered
Test.assert_equals(
    brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 
    'Codewars'
);

# Echo until byte(0) encountered
Test.assert_equals(
    brain_luck(',[.[-],]', 'Codewars' + chr(0)), 
    'Codewars'
);

# Two numbers multiplier
Test.assert_equals(
    brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), 
    chr(72)
)
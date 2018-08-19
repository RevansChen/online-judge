# Python - 3.4.3

Test.assert_equals(encode_rail_fence_cipher('WEAREDISCOVEREDFLEEATONCE', 3), 'WECRLTEERDSOEEFEAOCAIVDEN')
Test.assert_equals(encode_rail_fence_cipher('Hello, World!', 3), 'Hoo!el,Wrdl l')
Test.assert_equals(encode_rail_fence_cipher('Hello, World!', 4), 'H !e,Wdloollr')
Test.assert_equals(encode_rail_fence_cipher('', 3), '')

Test.assert_equals(decode_rail_fence_cipher('H !e,Wdloollr', 4), 'Hello, World!')
Test.assert_equals(decode_rail_fence_cipher('WECRLTEERDSOEEFEAOCAIVDEN', 3), 'WEAREDISCOVEREDFLEEATONCE')
Test.assert_equals(decode_rail_fence_cipher('', 3), '')
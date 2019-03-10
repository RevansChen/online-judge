# Python - 3.6.0

Test.assert_equals(split_and_merge('My name is John', ' '), 'M y n a m e i s J o h n')
Test.assert_equals(split_and_merge('My name is John', '-'), 'M-y n-a-m-e i-s J-o-h-n')
Test.assert_equals(split_and_merge('Hello World!', '.'), 'H.e.l.l.o W.o.r.l.d.!')
Test.assert_equals(split_and_merge('Hello World!', ','), 'H,e,l,l,o W,o,r,l,d,!')

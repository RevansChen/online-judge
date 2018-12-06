# Python - 2.7.6

Test.describe('Basic Tests')
Test.expect(ip_to_int32('128.114.17.104') == 2154959208, 'wrong integer for ip: 128.114.17.104')
Test.expect(ip_to_int32('0.0.0.0') == 0, 'wrong integer for ip: 0.0.0.0')
Test.expect(ip_to_int32('128.32.10.1') == 2149583361, 'wrong integer for ip: 128.32.10.1')

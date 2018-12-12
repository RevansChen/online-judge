# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(arrange(['200G', '300G', '150G', '100KG']), ['150G', '200G', '300G', '100KG'])
Test.assert_equals(arrange(['400G', '100T', '150KG', '100G']), ['100G', '400G', '150KG', '100T'])
Test.assert_equals(arrange(['4T', '300G', '450G', '900KG']), ['300G', '450G', '900KG', '4T'])
Test.assert_equals(arrange(['400T', '100T', '1T', '100G']), ['100G', '1T', '100T', '400T'])
Test.assert_equals(arrange(['1G', '2KG', '3T', '100KG']), ['1G', '2KG', '100KG', '3T'])
Test.assert_equals(arrange(['100KG', '100G', '150T', '150KG']), ['100G', '100KG', '150KG', '150T'])
Test.assert_equals(arrange(['3T', '2900000G', '2950KG']), ['2900000G', '2950KG', '3T'])
Test.assert_equals(arrange(['3T', '3000001G', '2950KG']), ['2950KG', '3T', '3000001G'])
Test.assert_equals(arrange(['1T']), ['1T'])
Test.assert_equals(arrange([]), [])

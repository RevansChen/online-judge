# Python - 2.7.6

collection = range(1, 25)
helper = PaginationHelper(collection, 10)

Test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
Test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
Test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')

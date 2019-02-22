# Python - 2.7.6

from math import ceil

class PaginationHelper:
    def __init__(self, collection, itemsPerPage):
        self.__collection = collection
        self.__itemsPerPage = itemsPerPage

    def item_count(self):
        return len(self.__collection)

    def page_count(self):
        return int(ceil(self.item_count() / float(self.__itemsPerPage)))

    def page_item_count(self, pageIndex):
        if (pageIndex < 0) or (pageIndex >= self.page_count()):
            return -1

        if (pageIndex + 1) == self.page_count():
            return self.item_count() % self.__itemsPerPage
        return self.__itemsPerPage

    def page_index(self, itemIndex):
        if (itemIndex < 0) or (itemIndex >= self.item_count()):
            return -1
        return itemIndex // self.__itemsPerPage

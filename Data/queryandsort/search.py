"""
排序实现：
"""


class Search:
    def __init__(self, list_, key):
        """

        :param list_:
        :param key:
        """
        self.list_ = list_
        self.key = key
        self.low = 0
        self.high = len(list_) - 1

    # 二分查找，数列是有序的
    def search(self):
        while self.low <= self.high:
            mid = (self.low + self.high) // 2
            if self.list_[mid] < self.key:
                self.low = mid + 1
            elif self.list_[mid] > self.key:
                self.high = mid - 1
            else:
                return mid
        return


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    s = Search(list, 6)
    print(s.search())

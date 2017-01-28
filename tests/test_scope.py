import unittest

from practice.scope import *


class TestScope(unittest.TestCase):
    def test_sorter1(self):
        _numbers = [2, 3, 4, 1, 9]
        sort_priority1(_numbers, {1, 9})
        self.assertListEqual(_numbers, [1, 9, 2, 3, 4])

    def test_sorter2(self):
        _numbers = [2, 3, 4, 1, 9]
        found = sort_priority2(_numbers, {1, 9})

        self.assertListEqual(_numbers, [1, 9, 2, 3, 4])
        self.assertFalse(found)

    def test_sorter3(self):
        _numbers = [2, 3, 4, 1, 9]
        found = sort_priority3(_numbers, {1, 9})

        self.assertListEqual(_numbers, [1, 9, 2, 3, 4])
        self.assertTrue(found)

    def test_sorter_class(self):
        _numbers = [2, 3, 4, 1, 9]
        _sorter = Sorter({1, 9})
        _numbers.sort(key=_sorter)

        self.assertListEqual(_numbers, [1, 9, 2, 3, 4])
        self.assertTrue(_sorter.found)


if __name__ == '__main__':
    unittest.main()

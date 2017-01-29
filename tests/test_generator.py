import unittest
from types import ListType, GeneratorType

from practice.generator import *


class TestGenerator(unittest.TestCase):
    def test_index_word(self):
        address = 'Four score and seven years ago'
        result = index_word(address)[:3]
        self.assertTrue(type(result) is ListType)
        self.assertListEqual(result, [0, 5, 11])

    def test_index_word_iter(self):
        address = 'Four score and seven years ago'
        generator = index_word_iter(address)
        self.assertTrue(type(generator) is GeneratorType)
        self.assertListEqual(list(generator)[:3], [0, 5, 11])


if __name__ == '__main__':
    unittest.main()

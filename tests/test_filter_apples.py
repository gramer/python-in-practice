import unittest

from practice.filter import Apple


class TestFilterApplesByListComprehensions(unittest.TestCase):
    def test_filter_by_lambda(self):
        inventory = [Apple('blue'), Apple('green')]
        filtered = [apple for apple in inventory if apple.color == 'blue']
        self.assertTrue(filtered)
        self.assertEqual(filtered[0].color, 'blue')


if __name__ == '__main__':
    unittest.main()

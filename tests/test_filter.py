import unittest

from practice.filter import Apple


class TestFilter(unittest.TestCase):
    def test_filter_by_list_comprehensions(self):
        inventory = [Apple('blue'), Apple('green')]
        filtered = [apple for apple in inventory if apple.color == 'blue']
        self.assertTrue(filtered)
        self.assertEqual(filtered[0].color, 'blue')

    # for fast and such as stream (save memory)
    def test_filter_by_generator_comprehensions(self):
        inventory = ["yellow", "blue"]
        it = (len(x) for x in inventory)

        self.assertEqual(next(it), len("yellow"))
        self.assertEqual(next(it), len("blue"))


if __name__ == '__main__':
    unittest.main()

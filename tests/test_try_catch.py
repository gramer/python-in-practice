import unittest
from practice.try_catch import divide


class TestTryError(unittest.TestCase):
    def test_divide_when_error(self):
        with self.assertRaises(ValueError):
            divide(0, 0)

    def test_divide(self):
        self.assertEqual(divide(1, 1), 1)


if __name__ == '__main__':
    unittest.main()

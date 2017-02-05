import unittest
from practice.args import *


class TestArguments(unittest.TestCase):
    def test_decode_wrong(self):
        foo = decode_wrong('bad data')
        foo['stuff'] = 5
        bar = decode_wrong('also bad')
        bar['meep'] = 1

        self.assertEqual(5, bar['stuff'])
        self.assertEqual(bar, foo)

    def test_decode_right(self):
        foo = decode_right('bad data')
        foo['stuff'] = 5
        bar = decode_right('also bad')
        bar['meep'] = 1

        with self.assertRaises(KeyError):
            bar['stuff']

    def test_divide_with_keyword_arguments(self):
        self.assertEqual(1, safe_division(1, 1, ignore_zero_div=True))
        self.assertEqual(float('inf'), safe_division(1, 0, ignore_zero_div=True))

        with self.assertRaises(ZeroDivisionError):
            safe_division(1, 0, ignore_zero_div=False)


if __name__ == '__main__':
    unittest.main()

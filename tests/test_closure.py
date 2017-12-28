import unittest

import practice.closure as closure


class TestClosure(unittest.TestCase):
    def test_closure(self):
        result = [multiplier(2) for multiplier in closure.create_multipliers()]
        self.assertListEqual(result, [0, 2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()

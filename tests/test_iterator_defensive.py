# coding=utf-8
import unittest
import tempfile
from practice.generator.iterator_defensive import *


class TestIteratorDefensive(unittest.TestCase):
    EXPECTED_AFTER_NORMALIZED = [16, 33, 50]
    VISITS = [10, 20, 30]

    def setUp(self):
        self.data_path = tempfile.mkstemp()[1]
        with open(self.data_path, 'w') as f:
            f.write("\n".join([str(x) for x in self.VISITS]))

    def test_normalize(self):
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, normalize(self.VISITS))

    def test_non_defensive_iterator(self):
        it = read_visits(self.data_path)
        percent = normalize(it)
        self.assertListEqual([], percent)

    def test_call_twice_generator(self):
        it = read_visits(self.data_path)
        self.assertListEqual(self.VISITS, list(it))
        self.assertListEqual([], list(it))

    def test_copy_iterator(self):
        it = read_visits(self.data_path)
        percent = normalize_copy(it)
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, percent)

    def test_new_iterator(self):
        percent = normalize_func(lambda: read_visits(self.data_path))
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, percent)

    def test_iter_protocol(self):
        percent = normalize(ReadVisits(self.data_path))
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, percent)

    def test_success_normalize_defensive(self):
        percent = normalize_defensive(ReadVisits(self.data_path))
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, percent)

        percent = normalize_defensive(self.VISITS)
        self.assertListEqual(self.EXPECTED_AFTER_NORMALIZED, percent)

    def test_throw_error_normalize_defensive(self):
        with self.assertRaises(TypeError):
            normalize_defensive(iter(self.VISITS))


if __name__ == '__main__':
    unittest.main()

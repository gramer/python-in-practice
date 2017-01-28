import unittest


class TestLoop(unittest.TestCase):
    def test_loop_by_enum(self):
        result = []
        flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
        for i, flavor in enumerate(flavor_list, 1):
            result.append("{0}:{1}".format(i, flavor))

        self.assertEqual(result[0], "1:vanilla")
        self.assertEqual(result[1], "2:chocolate")


if __name__ == '__main__':
    unittest.main()

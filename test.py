from quadratic import quadratic_func
import unittest


class Tests(unittest.TestCase):

    def test_1(self):  # simple testcase
        result = (-2.0, -3.0)
        self.assertEqual(result, quadratic_func(1, 5, 6))

    def test_2(self):
        result = (-1,)  # test_case for one solution ex: x1 will only return
        self.assertEqual(result, quadratic_func(1, 2, 1))

    def test_3(self):
        result = -1  # test_case for checking string values
        self.assertEqual(result, quadratic_func(1, "2", 1))

    def test_4(self):
        result = -1  # test_case for checking None
        self.assertEqual(result, quadratic_func(1, None, 1))

    def test_5(self):
        result = ((2+2j), (2-2j))  # checking answer for complex numbers
        self.assertEqual(result, quadratic_func(1, -4, 8))


if __name__ == '__main__':
    unittest.main()

import unittest
from func_test import fuction_test
class TestGameLogic(unittest.TestCase):
    def test_out_case(self):
        self.assertEqual(fuction_test(5, 5, 30), (30, "you are out!"))

    def test_continue_case(self):
        self.assertEqual(fuction_test(6, 5, 23), (29, "continue"))

    def test_invalid_case(self):
        self.assertEqual(fuction_test(-24, 4, 0), "invalid value!")

if __name__ == '__main__':
    unittest.main()

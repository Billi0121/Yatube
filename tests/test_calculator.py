# import unittest

# def serius_num(name):
#     return ''.join(str(i) for i in name)

# class TestSerius(unittest.TestCase):
#     def test_for_number(self):
#         number = '232'
#         self.assertEqual(serius_num([23232]), number, 'He is not working with nums')


# if __name__ == '__main__':
#     unittest.main()

import os
import sys
import unittest

# Добавим возможность импорта из директории code в наш тест
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR_PATH = os.path.join(BASE_DIR, 'code')
sys.path.append(CODE_DIR_PATH)

from calculator import MadCalculator

class TestMadCalculator(unittest.TestCase):
    """" Testing Madcalculator """

    def setUp(self):
        self.calc = MadCalculator()

    def test_sum_string(self):
        act = self.calc.sum_string(1, 10050)
        self.assertEqual(act, 110050, 'He is not working corectly' )

    def test_sum_args(self):
        act = self.calc.sum_args(3, 5, 4)
        self.assertEqual(act,  12, 'He is too match')
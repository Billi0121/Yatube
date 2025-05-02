# import unittest
# from code import series_sum  # Импорт тестируемой функции


# class TestSeriesSum(unittest.TestCase):
#     """Тестируем series_sum."""

#     def test_mixed_numbers(self):  # Это - test case
#         # Вызов тестируемой функции
#         call = series_sum([1, 2.5, 3, 4])
#         # Ожидаемый результат
#         result = '12.534'
#         # Проверка: идентичен ли результат вызова ожидаемому результату
#         self.assertEqual(
#             call, result,) ( 'Функция series_sum() не работает со списком чисел'
#         )

#     def test_mixed_numbers_strings(self):  # И это - test case
#         call = series_sum([1, 'fff', 3, 4])
#         result = '1fff34'
#         self.assertEqual(
#             call, result,) ('Функция series_sum не работает со смешанным списком'
#         )

#     def test_empty(self):  # И это - тоже test case
#         call = series_sum([])
#         result = ''
#         self.assertEqual(
#             call, result, 'Функция series_sum не работает с пустым списком'
#         )


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


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    def test_sum_string(self):
        # sum_string() возвращает конкатенированные строки
        calc = MadCalculator()
        act = calc.sum_string(1, 100500)
        self.assertEqual(act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_first_negative_value(self):
        calc = MadCalculator()
        # Проверяем, что при вызове метода sum_string() с отрицательным числом
        # в аргументе выбрасывается исключение ValueError
        self.assertRaises(ValueError, calc.sum_string, -1, 100500)

    def test_sum_string_second_negative_value(self):
        # Можно провести тестирование исключения,
        # использовав менеджер контекста
        calc = MadCalculator()
        with self.assertRaises(ValueError):
            calc.sum_string(1, -100500)

    def test_sum_args(self):
        # sum_args возвращает сумму принятых аргументов
        # Arrange - подготавливаем данные для теста.
        # Создаем экземпляр класса MadCalculator()
        calc = MadCalculator()

        # Act - выполнение тестируемого сценария.
        # Вызываем метод summ
        act = calc.sum_args(3, -3, 5)

        # Assert - проверяем, что метод работает
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.') 
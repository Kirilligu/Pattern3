import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Src.Logics.Convertors.basic_convertor import basic_convertor
from Src.Logics.Convertors.datetime_convertor import datetime_convertor
from Src.Logics.Convertors.reference_convertor import reference_convertor
from Src.Core.entity_model import entity_model
from datetime import datetime

class test_convertors(unittest.TestCase):
    """
    Тесты для конвертеров
    """
    def test_basic_convertor_simple_types(self):
        """
        Проверка basic_convertor на простых типах
        """
        # Подготовка
        converter = basic_convertor()

        # Создаем тестовый объект с простыми типами
        class TestObject:
            def __init__(self):
                self.name = "Тест"
                self.value = 123
                self.price = 45.67
                self.active = True

        test_obj = TestObject()

        # Действие
        result = converter.convert(test_obj)

        # Проверка
        self.assertEqual(result['name'], "Тест")
        self.assertEqual(result['value'], 123)
        self.assertEqual(result['price'], 45.67)
        self.assertEqual(result['active'], True)

    def test_datetime_convertor(self):
        """
        Проверка datetime_convertor
        """
        # Подготовка
        converter = datetime_convertor()
        test_date = datetime(2023, 12, 25, 14, 30, 0)

        # Действие
        result = converter.convert(test_date)

        # Проверка
        self.assertIn('datetime', result)
        self.assertIn('date', result)
        self.assertIn('time', result)
        self.assertEqual(result['datetime'], '2023-12-25T14:30:00')

    def test_reference_convertor(self):
        """
        Проверка reference_convertor
        """
        # Подготовка
        converter = reference_convertor()
        test_model = entity_model.create("Тестовая модель")

        # Действие
        result = converter.convert(test_model)

        # Проверка
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertEqual(result['name'], "Тестовая модель")
        self.assertEqual(len(result['id']), 32)  # UUID hex length

    def test_basic_convertor_skip_private(self):
        """
        Проверка что basic_convertor пропускает приватные атрибуты
        """
        # Подготовка
        converter = basic_convertor()

        class TestObject:
            def __init__(self):
                self.public = "публичное"
                self._private = "приватное"
                self.__very_private = "очень приватное"

        test_obj = TestObject()

        # Действие
        result = converter.convert(test_obj)

        # Проверка
        self.assertIn('public', result)
        self.assertNotIn('_private', result)
        self.assertNotIn('__very_private', result)

if __name__ == '__main__':
    unittest.main()
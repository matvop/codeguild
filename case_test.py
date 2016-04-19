import case
import unittest

class Conversion(unittest.TestCase):
    def test_convert_to_camel(self):
        found = case.convert_to_camel('snake_case')
        expected = 'SnakeCase'
        assert found == expected

    def test_camel_to_snake(self):
        found = case.camel_to_snake('SnakeCase')
        expected = 'snake_case'
        assert found == expected


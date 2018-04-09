# Модульное тестирование
import unittest
from our_strings import is_prefix

class TestOurString(unittest.TestCase):

    def test_is_prefix(self):
        s1 = "Nik"
        s2 = "Nikita"
        self.assertTrue(is_prefix(s1, s2))


if __name__ == '__main__':
    unittest.main()

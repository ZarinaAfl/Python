# Модульное тестирование
import unittest
from our_strings import is_prefix


params = [("Nik", "Nikita"), ("Tim", "Timur"), ("Danil", "Daniil")]


class TestOurString(unittest.TestCase):
    pass


def test_is_prefix(s1, s2):
    def test(self):
        self.assertTrue(is_prefix(s1, s2))
    return test()


test_case = TestOurString()
for i, pars in enumerate(params):
    test_name = "test" + str(i)
    setattr(test_case, test_name, test_is_prefix(pars[0], pars[1 ]))
import pytest

#связь тестов в определенную цепочку fixture
#объет может создаваться для каждого теста или модуля тестов

@pytest.fixture(scope="module")
def obj():
    class Password:
        def __init__(self):
            self.str = "parol"

    return Password()


def test_1(obj):
   assert obj.str == "parol"
   obj.str += "__salt"

def test_2(obj):
    assert obj.str == "parol__salt"


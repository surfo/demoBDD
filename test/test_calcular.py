from src import calculadora as calc

def test_suma():
    suma = calc.sumar(2,3)
    assert suma == 5


def test_resta():
    resta = calc.restar(4,4)
    assert resta == 0


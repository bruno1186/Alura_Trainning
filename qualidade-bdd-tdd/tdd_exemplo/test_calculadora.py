import pytest

from calculadora import Calculadora, ErroDivisaoPorZero


@pytest.fixture
def calculadora() -> Calculadora:
    return Calculadora()


def test_somar_dois_numeros_positivos(calculadora: Calculadora) -> None:
    assert calculadora.somar(2, 3) == 5


def test_subtrair_dois_numeros(calculadora: Calculadora) -> None:
    assert calculadora.subtrair(10, 4) == 6


def test_multiplicar_dois_numeros(calculadora: Calculadora) -> None:
    assert calculadora.multiplicar(3, 4) == 12


def test_dividir_dois_numeros(calculadora: Calculadora) -> None:
    assert calculadora.dividir(10, 2) == 5


def test_dividir_por_zero_lanca_erro(calculadora: Calculadora) -> None:
    with pytest.raises(ErroDivisaoPorZero):
        calculadora.dividir(10, 0)

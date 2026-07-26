"""
Calculadora simples, construída seguindo o ciclo TDD (Red-Green-Refactor).

Cada método aqui existe porque um teste em test_calculadora.py foi escrito
primeiro, exigindo a implementação mínima para passar.
"""


class ErroDivisaoPorZero(Exception):
    """Erro de domínio: divisão por zero não é permitida na calculadora."""


class Calculadora:
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ErroDivisaoPorZero("Não é possível dividir por zero.")
        return a / b

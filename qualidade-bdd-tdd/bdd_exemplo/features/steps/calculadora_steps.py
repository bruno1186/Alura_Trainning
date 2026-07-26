import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tdd_exemplo"))

from behave import given, then, when

from calculadora import Calculadora, ErroDivisaoPorZero


@given("que tenho uma calculadora")
def step_dado_calculadora(context):
    context.calculadora = Calculadora()
    context.erro = None
    context.resultado = None


@when("eu somo {a:d} e {b:d}")
def step_somar(context, a, b):
    context.resultado = context.calculadora.somar(a, b)


@when("eu divido {a:d} por {b:d}")
def step_dividir(context, a, b):
    try:
        context.resultado = context.calculadora.dividir(a, b)
    except ErroDivisaoPorZero as erro:
        context.erro = erro


@then("o resultado deve ser {esperado:d}")
def step_verifica_resultado(context, esperado):
    assert context.resultado == esperado, f"Esperado {esperado}, obtido {context.resultado}"


@then("devo receber um erro de divisão por zero")
def step_verifica_erro_divisao(context):
    assert isinstance(context.erro, ErroDivisaoPorZero), "Esperava um ErroDivisaoPorZero"

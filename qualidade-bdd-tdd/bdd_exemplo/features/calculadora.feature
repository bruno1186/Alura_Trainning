# language: pt

Funcionalidade: Operações da calculadora
  Como usuário da calculadora
  Eu quero realizar operações aritméticas básicas
  Para obter resultados corretos de forma confiável

  Cenário: Somar dois números positivos
    Dado que tenho uma calculadora
    Quando eu somo 2 e 3
    Então o resultado deve ser 5

  Cenário: Dividir um número por zero
    Dado que tenho uma calculadora
    Quando eu divido 10 por 0
    Então devo receber um erro de divisão por zero

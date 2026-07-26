# Qualidade de Software: TDD e BDD

Duas práticas complementares para construir software confiável, guiado por testes escritos antes (ou junto com) o código de produção.

## TDD (Test-Driven Development)

TDD é um ciclo curto e disciplinado: **Red → Green → Refactor**.

1. **Red:** escreva um teste que falha, descrevendo o comportamento que ainda não existe.
2. **Green:** escreva o código mínimo necessário para o teste passar.
3. **Refactor:** melhore o código (remova duplicação, melhore nomes) mantendo os testes verdes.

Esse ciclo curto força o design a nascer a partir do uso real da função/classe, resultando em interfaces mais simples e testáveis. O exemplo em [tdd_exemplo](./tdd_exemplo) implementa uma pequena calculadora seguindo esse ciclo, com testes em pytest.

## BDD (Behavior-Driven Development)

BDD desloca o foco de "testar unidades de código" para "descrever comportamento do sistema em linguagem natural", compreensível por pessoas técnicas e não técnicas. Cenários são escritos no formato Gherkin (**Dado / Quando / Então** — ou **Given / When / Then**), servindo tanto como documentação viva quanto como teste executável. O exemplo em [bdd_exemplo](./bdd_exemplo) descreve o comportamento da mesma calculadora usando um arquivo `.feature` executado com a biblioteca `behave`.

## Quando usar cada um

TDD é mais natural no nível de unidade — funções, classes e módulos isolados, com foco na equipe de desenvolvimento. BDD funciona melhor no nível de comportamento/funcionalidade de negócio, servindo como ponte de comunicação entre desenvolvedores, QA e stakeholders de negócio. Muitos times combinam os dois: BDD para descrever o comportamento esperado de uma funcionalidade, e TDD para guiar a implementação interna dos componentes que a compõem.

## Pirâmide de testes

Uma estratégia de testes saudável tem muitos testes unitários rápidos e baratos na base, uma quantidade média de testes de integração, e poucos testes end-to-end (mais lentos e caros de manter) no topo. Testes de comportamento (BDD) geralmente vivem no nível de integração/aceitação.

## Como rodar os exemplos

```bash
pip install -r requirements.txt

# Testes TDD (pytest)
pytest tdd_exemplo/

# Cenários BDD (behave)
behave bdd_exemplo/features/
```

Ambos são executados automaticamente no CI deste repositório (GitHub Actions).

## Boas práticas

- Testes devem ser rápidos, determinísticos e independentes entre si.
- Nomes de teste devem descrever o comportamento esperado, não a implementação.
- Cenários BDD devem refletir a linguagem do negócio, não detalhes técnicos internos.

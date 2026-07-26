# Ciência de Dados

Fluxo de trabalho para transformar dados em decisões, da pergunta de negócio ao modelo (quando fizer sentido usar um).

## O fluxo de um projeto de dados

1. **Definir a pergunta de negócio:** todo projeto de dados começa com uma pergunta clara e mensurável, não com "vamos usar machine learning".
2. **Coleta e entendimento dos dados:** de onde vêm os dados, com que frequência são atualizados, qual a granularidade disponível.
3. **Análise exploratória (EDA):** entender distribuições, outliers, valores faltantes e correlações antes de qualquer modelagem.
4. **Preparação dos dados:** limpeza, tratamento de valores faltantes, encoding de variáveis categóricas, normalização/padronização quando necessário.
5. **Modelagem (quando aplicável):** da regressão linear simples a modelos mais complexos — sempre começando pelo modelo mais simples que resolve o problema.
6. **Avaliação:** métricas alinhadas ao problema de negócio (nem sempre acurácia é a métrica certa — para dados desbalanceados, precisão/recall/F1 costumam ser mais informativos).
7. **Comunicação dos resultados:** um modelo ou análise só gera valor quando influencia uma decisão real.

## Análise exploratória de dados (EDA)

Antes de qualquer modelo, é essencial entender os dados: histogramas para distribuições, box plots para outliers, matrizes de correlação para relações entre variáveis, e verificação de valores nulos/duplicados. Grande parte do tempo de um projeto de dados é gasto aqui, não na modelagem.

## Estatística aplicada

Conceitos como média, mediana, desvio padrão, intervalos de confiança e testes de hipótese (ex: teste t, qui-quadrado) fundamentam decisões de negócio baseadas em dados — por exemplo, saber se a diferença observada entre dois grupos em um teste A/B é estatisticamente significativa ou apenas ruído.

## Introdução a Machine Learning

Aprendizado supervisionado (classificação, regressão) usa dados rotulados para prever um resultado. Aprendizado não supervisionado (clusterização, redução de dimensionalidade) encontra estrutura em dados sem rótulos. Regra prática: comece sempre com um baseline simples (ex: regressão logística) antes de partir para modelos mais complexos — o ganho de performance nem sempre justifica a perda de interpretabilidade.

## Exemplo prático

Este repositório inclui um script de exemplo ([analise_exemplo.py](./analise_exemplo.py)) que realiza uma análise exploratória simples com pandas sobre um conjunto de dados sintético de vendas.

## Boas práticas

- Validar a qualidade dos dados antes de confiar em qualquer conclusão.
- Preferir modelos simples e interpretáveis quando a diferença de performance para modelos complexos for pequena.
- Sempre separar dados de treino e teste para evitar overfitting e conclusões enganosas.

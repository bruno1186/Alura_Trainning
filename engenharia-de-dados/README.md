# Engenharia de Dados

Fundamentos para construir pipelines de dados confiáveis, do dado bruto até o dado pronto para consumo analítico.

## ETL vs ELT

**ETL (Extract, Transform, Load):** os dados são transformados antes de chegar ao destino final, geralmente fora do banco/data warehouse. **ELT (Extract, Load, Transform):** os dados brutos são carregados primeiro no destino (data warehouse/lakehouse) e transformados depois, aproveitando o poder de processamento de ferramentas como Snowflake, Databricks ou BigQuery. ELT se tornou o padrão dominante com a popularização de warehouses colunares de alta performance.

## Arquitetura em camadas (medallion)

Um padrão comum em lakehouses organiza os dados em três camadas:

- **Bronze:** dados brutos, exatamente como chegaram da fonte, com o mínimo de transformação (apenas parsing/schema).
- **Silver:** dados limpos, deduplicados, com tipos corrigidos e regras de qualidade aplicadas.
- **Gold:** dados agregados e modelados para consumo direto por times de negócio e ferramentas de BI.

## Modelagem de dados

Modelos dimensionais (star schema, com tabelas fato e dimensão) continuam sendo a base para data warehouses analíticos, otimizando consultas de BI. Já pipelines mais modernos com dbt favorecem modelagem em camadas (staging → intermediate → marts), com testes declarativos de qualidade em cada camada.

## Qualidade de dados

Pipelines de dados são tão confiáveis quanto os testes que os validam. Dimensões chave de qualidade: completude (faltam registros?), unicidade (há duplicatas indevidas?), validade (os valores respeitam o domínio esperado?), consistência (os dados batem entre diferentes fontes?) e atualidade (o dado está fresco o suficiente para a decisão que suporta?).

## Orquestração

Ferramentas como Apache Airflow, Dagster e orquestradores nativos de cada plataforma cloud coordenam a execução de pipelines com dependências entre etapas, retries automáticos e alertas em caso de falha.

## Exemplo prático

Este repositório inclui um pipeline de exemplo em Python ([pipeline_exemplo.py](./pipeline_exemplo.py)) que simula as camadas bronze/silver/gold com DuckDB. Um exemplo mais completo, com testes e CI, está disponível no repositório [data-lakehouse-etl](https://github.com/bruno1186/data-lakehouse-etl).

## Boas práticas

- Nunca sobrescrever dados brutos (bronze) — eles são a fonte da verdade para reprocessamento.
- Tornar pipelines idempotentes: rodar duas vezes com o mesmo input deve gerar o mesmo output.
- Testar dados como se testa código: validações automatizadas em cada camada.

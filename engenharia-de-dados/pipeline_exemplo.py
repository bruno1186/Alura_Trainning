"""
Pipeline de exemplo (bronze -> silver -> gold) usando DuckDB.

Objetivo didático: mostrar, de forma simples e executável, como estruturar
um pipeline de dados em camadas, incluindo uma validação básica de qualidade
antes de promover os dados para a camada seguinte.
"""

import duckdb


def criar_dados_brutos(con: duckdb.DuckDBPyConnection) -> None:
    """Camada bronze: dados exatamente como chegariam de uma fonte externa."""
    con.execute(
        """
        CREATE TABLE bronze_pedidos AS
        SELECT * FROM (
            VALUES
                (1, 'cliente_a', 150.00, '2026-01-05'),
                (2, 'cliente_b', -10.00, '2026-01-06'),
                (3, 'cliente_a', 200.50, '2026-01-06'),
                (4, NULL,        75.00, '2026-01-07')
        ) AS t(id_pedido, cliente, valor, data_pedido)
        """
    )


def validar_qualidade(con: duckdb.DuckDBPyConnection) -> list:
    """Regras simples de qualidade: valor deve ser positivo e cliente não nulo."""
    problemas = con.execute(
        """
        SELECT id_pedido, cliente, valor
        FROM bronze_pedidos
        WHERE valor <= 0 OR cliente IS NULL
        """
    ).fetchall()
    return problemas


def transformar_para_silver(con: duckdb.DuckDBPyConnection) -> None:
    """Camada silver: remove registros inválidos e normaliza tipos."""
    con.execute(
        """
        CREATE TABLE silver_pedidos AS
        SELECT
            id_pedido,
            cliente,
            valor,
            CAST(data_pedido AS DATE) AS data_pedido
        FROM bronze_pedidos
        WHERE valor > 0 AND cliente IS NOT NULL
        """
    )


def agregar_para_gold(con: duckdb.DuckDBPyConnection) -> None:
    """Camada gold: dados agregados prontos para consumo analítico."""
    con.execute(
        """
        CREATE TABLE gold_receita_por_cliente AS
        SELECT cliente, SUM(valor) AS receita_total, COUNT(*) AS total_pedidos
        FROM silver_pedidos
        GROUP BY cliente
        ORDER BY receita_total DESC
        """
    )


def executar_pipeline() -> None:
    con = duckdb.connect(database=":memory:")

    criar_dados_brutos(con)

    problemas = validar_qualidade(con)
    if problemas:
        print(f"Aviso: {len(problemas)} registro(s) com problema de qualidade na camada bronze:")
        for p in problemas:
            print(f"  - id_pedido={p[0]} cliente={p[1]} valor={p[2]}")

    transformar_para_silver(con)
    agregar_para_gold(con)

    resultado = con.execute("SELECT * FROM gold_receita_por_cliente").fetchall()
    print("\nReceita agregada por cliente (camada gold):")
    for linha in resultado:
        print(f"  cliente={linha[0]} receita_total={linha[1]} total_pedidos={linha[2]}")

    con.close()


if __name__ == "__main__":
    executar_pipeline()

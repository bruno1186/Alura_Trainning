"""
Exemplo didático de análise exploratória de dados (EDA) com pandas.

Gera um conjunto de dados sintético de vendas e demonstra os passos
básicos de uma EDA: inspeção inicial, estatísticas descritivas,
detecção de valores nulos/outliers e uma agregação simples.
"""

import numpy as np
import pandas as pd


def gerar_dados_sinteticos(n: int = 200, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    categorias = rng.choice(["eletronicos", "moda", "casa", "esporte"], size=n)
    valores = rng.normal(loc=150, scale=60, size=n).round(2)
    valores[rng.choice(n, size=5, replace=False)] = np.nan  # simula valores faltantes
    valores[rng.choice(n, size=3, replace=False)] *= 8  # simula outliers

    df = pd.DataFrame(
        {
            "categoria": categorias,
            "valor_venda": valores,
        }
    )
    return df


def resumo_estatistico(df: pd.DataFrame) -> pd.DataFrame:
    return df["valor_venda"].describe()


def detectar_outliers_iqr(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]


def agregar_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.dropna(subset=["valor_venda"])
        .groupby("categoria")["valor_venda"]
        .agg(["count", "mean", "sum"])
        .rename(columns={"count": "qtd_vendas", "mean": "ticket_medio", "sum": "receita_total"})
        .sort_values("receita_total", ascending=False)
    )


def main() -> None:
    df = gerar_dados_sinteticos()

    print("Amostra dos dados:")
    print(df.head())

    print("\nValores nulos por coluna:")
    print(df.isna().sum())

    print("\nEstatísticas descritivas de valor_venda:")
    print(resumo_estatistico(df))

    outliers = detectar_outliers_iqr(df.dropna(subset=["valor_venda"]), "valor_venda")
    print(f"\nOutliers detectados (regra IQR): {len(outliers)}")

    print("\nAgregação por categoria:")
    print(agregar_por_categoria(df))


if __name__ == "__main__":
    main()

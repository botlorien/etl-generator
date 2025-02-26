import itertools
import pandas as pd
import sqlite3 as sq
from collections.abc import Iterable, Iterator


def extrair_dados(nome_arquivo, length=10) -> Iterator:
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        colunas = tuple(f.readline().strip().split(';'))
        counter = itertools.count()
        bloco = [colunas]
        for linha in f:
            bloco.append(tuple(linha.strip().split(';')))
            if len(bloco) >= length + 1:
                yield bloco, next(counter)
                bloco = [colunas]

        if len(bloco) > 1:
            yield bloco, next(counter)


def tranformar_dados(dados: Iterable) -> Iterator:
    for lote, i in dados:
        print(lote)
        df = pd.DataFrame(
            lote[1:],
            columns=lote[0]
        )
        print(df)
        yield df, i


def carregar_dados_no_banco(dados: Iterable) -> Iterator:
    for lote, i in dados:
        lote: pd.DataFrame

        print(f"Inserindo lote {i} no banco de dados...")

        table_name = 'dados_ficticios'
        conn = sq.connect('{}.sqlite'.format(table_name))
        lote.to_sql(table_name, conn, if_exists='append', index=False)
        conn.close()

        yield f"Lote {i} inserido com sucesso!"


if __name__ == '__main__':
    extrator = extrair_dados('dados_ficticios.csv')
    transformer = tranformar_dados(extrator)
    loader = carregar_dados_no_banco(transformer)

    for status in loader:
        print(status)
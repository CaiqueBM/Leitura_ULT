import pandas as pd
import sqlite3


def transformar():
    # Conectar ao banco de dados SQLite (substitua 'seu_banco_de_dados.db' pelo nome do seu banco de dados)
    conexao = sqlite3.connect("dados.db")

    # Consulta SQL para recuperar os dados da tabela desejada (substitua 'sua_tabela' pelo nome da sua tabela)
    consulta_sql = "SELECT * FROM dados"

    # Use o método read_sql_query do pandas para executar a consulta e obter os resultados em um DataFrame
    dados_dataframe = pd.read_sql_query(consulta_sql, conexao)

    # Fechar a conexão com o banco de dados
    conexao.close()

    # Salvar o DataFrame em um arquivo CSV (substitua 'saida.csv' pelo nome desejado para o arquivo CSV)
    dados_dataframe.to_csv("saida_day.csv", index=False, sep=";")

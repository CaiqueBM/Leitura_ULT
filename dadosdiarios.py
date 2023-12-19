import requests
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
from dados import gerar_tabelas
from SQLtoCSV import transformar
from envio import enviar_mensagem
from carregar import recarregar_pagina


gerar_tabelas()
recarregar_pagina()

ids = [578496, 667618, 686932]

data_atual = datetime.now().strftime("%Y-%m-%d")

resultados = []
df = pd.DataFrame()

for usina_id in ids:
    valores_data = []
    valores_quantidade = []
    valores_denominacao = []

    nova_url = f"https://app.solarz.com.br/shareable/generation/period?usinaId={usina_id}&start={data_atual}&end={data_atual}&uniteMonths=false"

    # Obter os dados da URL
    response = requests.get(nova_url)

    # Verifique se a resposta foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        data = response.json()
        dados = data.get("dados", [])

        for item in dados:
            valores_data.append(item["data"])
            valores_quantidade.append(
                str(item["quantidade"]).replace(".", ",")
            )  # Modificação aqui
            valores_denominacao.append(item["denominacao"])

    df_usina = pd.DataFrame(
        {
            "DATA": valores_data,
            "GERACAO": valores_quantidade,
            "ULT": valores_denominacao,
        }
    )

    df = pd.concat([df, df_usina], ignore_index=True)

# Conectar ao banco de dados e salvar o DataFrame
conn = sqlite3.connect("dados.db")
df.to_sql(
    "dados", conn, index=False, if_exists="append"
)  # Use "replace" se desejar substituir a tabela existente
conn.close()

# Atualizar o arquivo CSV
transformar()

# Enviar mensagem para Whatsapp
enviar_mensagem(df)

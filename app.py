from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    # Conecte-se ao banco de dados
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()

    # Execute a consulta SQL para obter nomes únicos de ULT
    cursor.execute("SELECT DISTINCT ULT FROM dados_diarios")
    nomes_ult = [row[0] for row in cursor.fetchall()]

    # Feche a conexão com o banco de dados
    conn.close()
    return render_template("index.html", nomes_ult=nomes_ult)


@app.route("/resultado", methods=["POST"])
def resultado():
    data_inicial = request.form["data_inicial"]
    data_final = request.form["data_final"]
    nome_ult = request.form["nome_ult"]

    data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y").strftime("%Y-%m-%d")
    data_final = datetime.strptime(data_final, "%d/%m/%Y").strftime("%Y-%m-%d")

    # Conecte-se ao banco de dados
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    print(
        f"Data Inicial: {data_inicial}, Data Final: {data_final}, Nome ULT: {nome_ult}"
    )

    # Execute a consulta SQL com base nos parâmetros
    query = """
    SELECT DATA, GERACAO FROM dados_diarios
    WHERE DATA BETWEEN ? AND ?
    AND ULT = ?
    """
    cursor.execute(query, (data_inicial, data_final, nome_ult))
    resultados = cursor.fetchall()
    resultados = [(datetime.strptime(row[0], "%Y-%m-%d"), row[1]) for row in resultados]

    # Calcule a soma da coluna GERACAO
    sum_geracao = sum(float(resultado[1].replace(",", ".")) for resultado in resultados)
    sum_geracao = round(sum_geracao, 2)
    sum_geracao = str(sum_geracao) + " kWh"

    # Feche a conexão com o banco de dados
    conn.close()

    data_inicial_obj = datetime.strptime(data_inicial, "%Y-%m-%d")
    data_inicial_formatada = data_inicial_obj.strftime("%d/%m/%Y")
    data_final_obj = datetime.strptime(data_final, "%Y-%m-%d")
    data_final_formatada = data_final_obj.strftime("%d/%m/%Y")

    return render_template(
        "resultado.html",
        resultados=resultados,
        sum_geracao=sum_geracao,
        data_inicial=data_inicial_formatada,
        data_final=data_final_formatada,
    )


if __name__ == "__main__":
    app.run(debug=True)

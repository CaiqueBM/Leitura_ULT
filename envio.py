import pandas as pd
import pywhatkit
from datetime import datetime


# --------------------- MENSAGEM WHATSAPP ------------------------
def enviar_mensagem(df):
    mensagem_whatsapp = (
        f"Geração total diária: \r\n"
        f"⚡"
        f"{df.loc[df['ULT'] == 'ULT - 1', 'ULT'].iloc[0]} - {df.loc[df['ULT'] == 'ULT - 1', 'GERACAO'].iloc[0]} kWh \r\n"
        f"⚡"
        f"{df.loc[df['ULT'] == 'ULT 3 - Back Up ', 'ULT'].iloc[0]} - {df.loc[df['ULT'] == 'ULT 3 - Back Up ', 'GERACAO'].iloc[0]} kWh \r\n"
        f"⚡"
        f"{df.loc[df['ULT'] == 'ULT - 4', 'ULT'].iloc[0]} - {df.loc[df['ULT'] == 'ULT - 4', 'GERACAO'].iloc[0]} kWh"
    )

    pywhatkit.sendwhatmsg_instantly("+5527996162054", mensagem_whatsapp, 10, False, 15)


# --------------------- MENSAGEM EMAIL ---------------------------
def enviar_email():
    titulo_email = "Geração mensal"
    mensagem_email = (
        "Geração total mensal: ULT 1 - 150 kWh | ULT 3 - 400 kWh | ULT 4 - 50 kWh"
    )
    # ---------------------------------------------------
    agora = datetime.now()
    if agora.day == 1:
        print("teste2")
        pywhatkit.send_mail(
            "sistemasabsengenharia@gmail.com",
            "wmog wgxt gwcm mpxs",
            titulo_email,
            mensagem_email,
            "caiquemaso23@gmail.com",
        )

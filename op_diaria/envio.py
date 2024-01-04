import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time


# --------------------- MENSAGEM  WHATSAPP ------------------------
def enviar_mensagem(df):
    mensagem_whatsapp = (
        f"Geração total diária: %0A"
        f"◉"
        f"{df.loc[df['ULT'] == 'ULT - 1', 'ULT'].iloc[0]}: {df.loc[df['ULT'] == 'ULT - 1', 'GERACAO'].iloc[0]} kWh %0A"
        f"◉"
        f"{df.loc[df['ULT'] == 'ULT 2', 'ULT'].iloc[0]}: {df.loc[df['ULT'] == 'ULT 2', 'GERACAO'].iloc[0]} kWh %0A"
        f"◉"
        f"{df.loc[df['ULT'] == 'ULT 3 - Back Up ', 'ULT'].iloc[0]}: {df.loc[df['ULT'] == 'ULT 3 - Back Up ', 'GERACAO'].iloc[0]} kWh %0A"
        f"◉"
        f"{df.loc[df['ULT'] == 'ULT - 4', 'ULT'].iloc[0]}: {df.loc[df['ULT'] == 'ULT - 4', 'GERACAO'].iloc[0]} kWh %0A"
    )

    mensagem_codificada = mensagem_whatsapp

    #  m ensagem_codificada = quote(mensagem_whatsapp222)

    options = webdriver.ChromeOptions()
    # options.binary_location  = "/usr/local/bin/chromedriver"
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    # options.add_argument("--enable-logging --v=1")
    # provide location where chrome stores profiles
    options.add_argument(r"--user-data-dir=/home/abs/.config/google-chrome")

    # provide the profile name with which we want to open browser
    options.add_argument(r"--profile-directory=Profile 1")

    # options.add_argument("--user-data-dir=/Home/.config/google-chrome")  # Path to your chrome profile
    # options.add_argument("--profile-directory=Profile 1")  # Path to your chrome profile
    driver = webdriver.Chrome(options=options)

    # options = webdriver.ChromeOptions()

    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)

    numero = "+5527996162054"

    url = "https://wa.me//" + numero + "?text=" + mensagem_codificada
    # url = "https://whatsa.me/" + numero + "/?t=" + mensagem_whatsapp

    # ULT 1
    driver.get(url)

    time.sleep(20)

    # pywhatkit.sendwhatmsg_instantly("+5527999438898", mensagem_whatsapp, 10, False, 15)

    button = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a",
    )
    time.sleep(5)
    button.click()
    time.sleep(5)

    button1 = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a",
    )
    time.sleep(5)
    button1.click()
    time.sleep(100)

    button2 = driver.find_element(
        By.XPATH,
        "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button",
    )
    time.sleep(2)
    button2.click()
    time.sleep(5)

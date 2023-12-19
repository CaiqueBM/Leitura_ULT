from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def recarregar_pagina():
    # Configuração do Selenium

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    url_att1 = f"https://pages.solarz.com.br/shareable/usina/f80e8b26-d0f3-4735-a19a-015b4c1092fe"
    url_att2 = f"https://pages.solarz.com.br/shareable/usina/c81109eb-cedc-4e89-8bc7-c7e643109806"
    url_att3 = f"https://pages.solarz.com.br/shareable/usina/43c93787-d85d-4e30-8154-317157c6750e"

    # ULT 1
    driver.get(url_att1)
    time.sleep(10)
    button1 = driver.find_element(
        By.XPATH,
        "//*[@id='__next']/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/label[1]/div",
    )
    button1.click()
    time.sleep(10)

    # ULT 3
    driver.get(url_att2)
    time.sleep(10)
    button2 = driver.find_element(
        By.XPATH,
        "//*[@id='__next']/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/label[1]/div",
    )
    button2.click()
    time.sleep(10)

    # ULT 4
    driver.get(url_att3)
    time.sleep(10)
    button3 = driver.find_element(
        By.XPATH,
        "//*[@id='__next']/div/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/label[1]/div",
    )
    button3.click()
    time.sleep(10)

    # Fechar o navegador
    # driver.quit()
    driver.quit

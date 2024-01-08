import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mensagem_whatsapp = f"Geração total diária: %0A" f"◉"

mensagem_codificada = mensagem_whatsapp

#  mensagem_codificada = quote(mensagem_whatsapp222)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.binary_location = "/usr/local/bin/chromedriver"
options.add_argument("--no-sandbox")
options.add_argument("--user-data-dir=/home/abs/.config/google-chrome")
# provide the profile name with which we want to open browser
options.add_argument("--profile-directory=Profile 4")
# options.add_argument("--enable-logging --v=1")
driver = webdriver.Chrome(options=options)

# options.add_argument("--user-data-dir=/home/abs/.config/google-chrome/Profile 4")
# options.add_argument("--profile-directory=Profile 4")
# driver = webdriver.Chrome(options=options)

numero = "+5527996162054"

url = "https://wa.me//" + numero + "?text=" + mensagem_codificada
# url = "https://whatsa.me/" + numero + "/?t=" + mensagem_whatsapp

# ULT 1
driver.get(url)

time.sleep(60)

# pywhatkit.sendwhatmsg_instantly("+5527999438898", mensagem_whatsapp, 10, False, 15)

button = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a",
)
time.sleep(10)
button.click()
time.sleep(10)

button1 = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a",
)
time.sleep(5)
button1.click()
time.sleep(100)

"""button2 = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button",
)
time.sleep(2)
button2.click()
time.sleep(5)"""


"""button2 = driver.find_element(
    "xpath",
    "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p",
)
button2.send_keys(Keys.ENTER)
time.sleep(5)"""

# Espera até que o elemento seja visível (pode ajustar o timeout conforme necessário)
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p",
        )
    )
)
element.click()


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Pendiente
from webdriver_manager.chrome import ChromeDriverManager

S = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service= S, options=opc)
navegador.get("https://es-la.facebook.com/")

txtEmail = navegador.find_element(By.NAME,"email")
txtEmail.send_keys("usuario@gmail.com")

txtpassword = navegador.find_element(By.NAME,"pass")
txtpassword.send_keys("****************")

time.sleep(5)

navegador.save_screenshot("img_test.png")

btnlogin = navegador.find_element(By.NAME, "login")
btnlogin.click()

navegador.find_elements()

time.sleep(10)
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del servicio y opciones de Chrome
s = Service(ChromeDriverManager().install())
opciones = Options()
opciones.add_argument("--window-size=1020,1200")

# Iniciar el navegador
navegador = webdriver.Chrome(service=s, options=opciones)

# Realizar una solicitud GET a la página de Amazon
response = requests.get("https://www.amazon.com.mx/")
print(response.status_code)

# Comprobar si la solicitud fue exitosa antes de continuar
if response.status_code == 200:

    # Localizar el campo de búsqueda y realizar la búsqueda
    campo_busqueda = navegador.find_element(By.NAME, "field-keywords")
    campo_busqueda.send_keys("Jurassic Park (Spanish Edition)")
    campo_busqueda.submit()

    # Esperar un tiempo para cargar los resultados de búsqueda
    time.sleep(5)

    data = {
        "Nombre": [],
        "Calificacion": [],
        "Entrega": [],
        "Precio": []
    }

    # Recopilar datos de los resultados de búsqueda
    resultados = navegador.find_elements(By.CSS_SELECTOR, "div.s-result-item")

    for resultado in resultados:
        nombre = resultado.find_element(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
        calificacion = resultado.find_element(By.CSS_SELECTOR, "span.a-size-base.puis-normal-weight-text")
        entrega = resultado.find_element(By.CSS_SELECTOR, "span.a-color-base.a-text-bold")
        precio = resultado.find_element(By.CSS_SELECTOR, "span.a-price-whole")

        data["Nombre"].append(nombre.text)
        data["Calificacion"].append(calificacion.text)
        data["Entrega"].append(entrega.text.strip())
        data["Precio"].append(precio.text)

    # Cerrar el navegador
    navegador.quit()

    # Convertir los datos a un DataFrame de Pandas y guardar en un archivo CSV
    data_df = pd.DataFrame(data)
    data_df.to_csv("amazon.csv", index=False)

else:
    print(f"No se pudo acceder a la página de Amazon. Código de estado: {response.status_code}")

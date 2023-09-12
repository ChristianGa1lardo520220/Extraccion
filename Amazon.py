import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuración del servicio y opciones de Chrome
s = Service(ChromeDriverManager().install())
opciones = Options()
opciones.add_argument("--window-size=1020,1200")

# Iniciar el navegador
navegador = webdriver.Chrome(service=s, options=opciones)

# Navegar a la página de Amazon
navegador.get("https://www.amazon.com./-/es/qp/navigation-country/")

# Localizar el campo de búsqueda y realizar la búsqueda
campo_busqueda = navegador.find_element(By.NAME, "field-keywords")
campo_busqueda.send_keys("Hello Kitty")
campo_busqueda.submit()

# Esperar un tiempo para cargar los resultados de búsqueda
time.sleep(5)

datos = {
    "Nombre del producto": [],
    "Precio": [],
    "Tiempo de entrega": [],
    "Calificacion": []
}

# Recopilar datos de los resultados de búsqueda
resultados = navegador.find_elements(By.TAG_NAME, "div")
for resultado in resultados:
    try:
        nombre_producto = resultado.find_element(By.TAG_NAME, "a-size-base-plus a-color-base a-text-normal").text
    except:
        nombre_producto = "No se encontró nombre del producto"

    try:
        precio = resultado.find_element(By.CLASS_NAME, "a-price-whole").find_element(By.TAG_NAME, "span").text
    except:
        precio = "Precio no disponible"

    try:
        tiempo_entrega = resultado.find_element(By.CLASS_NAME, "a-color-base a-text-bold").text
    except:
        tiempo_entrega = "Tiempo de entrega no disponible"

    try:
        calificacion = resultado.find_element(By.CSS_SELECTOR, "a-size-base puis-normal-weight-text").text
    except:
        calificacion = "Calificación no disponible"

    datos["Nombre del producto"].append(nombre_producto)
    datos["Precio"].append(precio)
    datos["Tiempo de entrega"].append(tiempo_entrega)
    datos["Calificacion"].append(calificacion)

# Cerrar el navegador
navegador.quit()

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(datos)

# Imprimir el DataFrame
print(df)

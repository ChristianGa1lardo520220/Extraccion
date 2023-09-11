import time  # Importa la biblioteca 'time' para pausas en el script.
import pandas as pd  # Importa la biblioteca 'pandas' para trabajar con DataFrames.
from selenium import webdriver  # Importa el módulo 'webdriver' de Selenium para automatización web.
from selenium.webdriver.chrome.service import Service  # Importa 'Service' para configurar el controlador de Chrome.
from selenium.webdriver.chrome.options import Options  # Importa 'Options' para configurar las opciones de Chrome.
from selenium.webdriver.common.by import By  # Importa 'By' para seleccionar elementos en la página web.
from webdriver_manager.chrome import ChromeDriverManager  # Importa 'ChromeDriverManager' para gestionar el controlador de Chrome.
from bs4 import BeautifulSoup  # Importa 'BeautifulSoup' para analizar el HTML de la página web.

# Configura el servicio de Chrome usando 'ChromeDriverManager' para descargar el controlador adecuado.
S = Service(ChromeDriverManager().install())

# Configura las opciones de Chrome, como el tamaño de la ventana.
opc = Options()
opc.add_argument("--window-size=1020,1200")

# Inicializa el navegador Chrome con el servicio y opciones configurados.
navegador = webdriver.Chrome(service=S, options=opc)

# Abre la página web deseada en el navegador.
navegador.get("http://www.olympedia.org/statistics/medal/country")

# Encuentra elementos en la página web utilizando el método 'find_element' de Selenium.
cmbYear = navegador.find_element(By.NAME, "edition_id")  # Encuentra el elemento de selección de año.
cmbGenero = navegador.find_element(By.NAME, "athlete_gender")  # Encuentra el elemento de selección de género.

# Encuentra las opciones dentro de los elementos de selección de género y año.
genderOption = cmbGenero.find_elements(By.TAG_NAME, "option")
yearsGroups = cmbYear.find_elements(By.TAG_NAME, "optgroup")
year_list = yearsGroups[0].find_elements(By.TAG_NAME, "option")

# Crea un diccionario vacío 'datos' para almacenar los datos extraídos.
datos = {
    "Country": [],
    "Year": [],
    "Gender": [],
    "Gold": [],
    "Silver": [],
    "Bronce": [],
    "Total": []
}

# Itera a través de las opciones de género (excluyendo la primera opción vacía).
for gender in genderOption[1:]:
    gender.click()  # Selecciona una opción de género.

    # Itera a través de las opciones de año.
    for year in year_list:
        year.click()  # Selecciona un año.
        time.sleep(1)  # Espera 1 segundo para que la página se cargue completamente.

        # Analiza el HTML de la página web utilizando BeautifulSoup.
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        tabla = soup.find("table", attrs={"class": "table table-striped"})  # Encuentra la tabla de datos.
        list_ross = tabla.find_all("tr")  # Encuentra todas las filas de la tabla.

        # Itera a través de las filas de la tabla (excluyendo la primera fila de encabezados).
        for row in list_ross[1:]:
            datos["Gender"].append(gender.text)
            datos["Year"].append(year.text)
            values = row.find_all("td")  # Encuentra todas las celdas de la fila.
            datos["Country"].append(values[0].text)
            datos["Gold"].append(values[2].text)
            datos["Silver"].append(values[3].text)
            datos["Bronce"].append(values[4].text)
            datos["Total"].append(values[5].text)

# Cierra el navegador web.
navegador.close()

# Convierte el diccionario 'datos' en un DataFrame de pandas.
data_df = pd.DataFrame(datos)

# Guarda el DataFrame en un archivo CSV llamado "data_olimpiadas.csv".
data_df.to_csv("data_olimpiadas.csv")

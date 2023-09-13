import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def buscar_y_capturar_amazon(producto):
    try:
        s = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--window-size=1020,1200")


        navegador = webdriver.Chrome(service=s, options=options)
        navegador.get("https://www.amazon.co.jp/")

        txtbusqueda = navegador.find_element(By.NAME, "field-keywords")

        txtbusqueda.clear()

        for letra in producto:
            txtbusqueda.send_keys(letra)
            time.sleep(1.6)  # Pausa de 0.5 segundos entre cada letra

        txtbusqueda.send_keys(Keys.RETURN)

        time.sleep(5)  # Pausa después de la búsqueda

        navegador.save_screenshot("img_amazon.png")

        time.sleep(10)  # Pausa adicional antes de cerrar el navegador

        navegador.quit()

        print(
            f"Búsqueda de '{producto}' en Amazon realizada con éxito. Captura de pantalla guardada como 'img_amazon.png'.")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        navegador.quit()

if __name__ == "__main__":
    producto = input("Ingrese el nombre del producto a buscar en Amazon: ")
    buscar_y_capturar_amazon(producto)

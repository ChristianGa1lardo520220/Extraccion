
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
#print(response.content)
textos = []
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    lista_divs = soup.find_all("div", attrs={"class":"card-content"})
#print(soup.head.title.text)
    data = {
        "puesto": [],
        "empresa": [],
        "ciudad":[],
        "fecha": []
    }

    for div in lista_divs:
        puesto = div.find("h2", attrs={"class":"title is-5"})
        company = div.find("h3", attrs={"class":"subtitle is-6 company"})
        ciudad = div.find("p", attrs={"class":"location"})
        fecha = div.find("time")
        data["puesto"].append(puesto.text)
        data["empresa"].append(company.text)
        data["ciudad"].append(ciudad.text.strip())
        data["fecha"].append(fecha.text)

    data_df = pd.DataFrame(data)
    data_df.to_csv("datasets/jobs.csv")

else:
    print(f"no se pudo por el error {response.status_code}")

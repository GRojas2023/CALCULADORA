import requests
from bs4 import BeautifulSoup

url = "https://dolarhoy.com/"

# Realiza la solicitud GET a la página web
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra el elemento que contiene el precio del dólar
    # Esto puede requerir inspeccionar el HTML de la página para encontrar el selector adecuado
    dolar_element = soup.find("span", {"class": "data-venta"})

    # Obtiene el precio del dólar
    if dolar_element:
        precio_dolar = dolar_element.text
        print(f"El precio del dólar hoy es: {precio_dolar}")
    else:
        print("No se pudo encontrar el precio del dólar en la página.")

else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")

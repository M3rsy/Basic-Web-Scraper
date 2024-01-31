import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # REALIZA UNA SOLICITUD HTTP PARA OBTENER EL CONTENIDO DE LA PÁGINA
    response = requests.get(url)
    if response.status_code != 200:
        print("Error al acceder a la página")
        return

    # UTILIZA BEAUTIFULSOUP PARA ANALIZAR EL HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # EXTRAER INFORMACIÓN ESPECÍFICA, EJEMPLO: TÍTULOS
    for title in soup.find_all('h2'):  # CAMBIA 'h2' POR LA ETIQUETA APROPIADA
        print(title.get_text())

# URL DE LA PÁGINA A SCRAPEAR
url = 'https://www.hackthissite.org/'
scrape_website(url)

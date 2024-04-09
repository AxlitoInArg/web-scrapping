import requests
from bs4 import BeautifulSoup

def obtener_cotizaciones(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    coti_table = soup.find("tbody")
    trs = coti_table.find_all("tr")
    cotizaciones = {}
    for tr in trs:
        td = tr.find_all("td")
        moneda = td[0].text.strip()
        valor = td[2].text.strip()
        cotizaciones[moneda] = valor
    return cotizaciones

url = "https://www.bna.com.ar/Personas"
cotizaciones = obtener_cotizaciones(url)

if cotizaciones:
    print("Cotizaciones:")
    print("Dólar U.S.A:", cotizaciones.get("Dolar U.S.A", "No disponible"))
else:
    print("La página está caida.")

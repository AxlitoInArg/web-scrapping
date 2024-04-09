import requests
from bs4 import BeautifulSoup

def obtener_cotizacion_banco_provincia(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    cotizacion_div = soup.find("div", {"aria-label": "Cotización del dólar"})
    if cotizacion_div:
        cotizacion_texto = cotizacion_div.find_next("div", class_="paginas__sc-1t8sitw-1 dgBaJN")
        if cotizacion_texto:
            return cotizacion_texto.text.strip()
    return None

url_banco_provincia = "https://www.bancoprovincia.com.ar/home/"
cotizacion_dolar = obtener_cotizacion_banco_provincia(url_banco_provincia)

if cotizacion_dolar:
    print("Cotización del dólar en Banco Provincia:", cotizacion_dolar)
else:
    print("No se encontró la cotización del dólar en la página del Banco Provincia.")
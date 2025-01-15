import requests #pip install requests


def obtener_clima(ciudad):
    api_key = 'tu_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
    response = requests.get(url).json()

    if response.get("main"):
        print(f"Clima en {ciudad}: {response['main']['temp']}°C")
    else:
        print("Ciudad no encontrada.")

# Ejemplo de uso
obtener_clima("Mexico")

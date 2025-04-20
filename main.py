import requests
import json

lat = -12.97
lon = -38.51


key = "c738918cb6f4bdc66c16e695937b6a4b"
""" url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}" """
url = f"https://api.openweathermap.org/data/2.5/weather?q=Brasilia&appid={key}"

request = requests.get(url)
resposta = request.json()
for key, value in resposta.items():
    print(f"{key}: {value}")

print (resposta['main']['humidity'])
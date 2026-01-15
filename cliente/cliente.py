import urllib.request
import json

# OJO: Aquí usamos el nombre del contenedor servidor, no localhost
url = "http://servidor-api:5000"

print("--- INICIANDO CLIENTE EN LA RED DOCKER ---")

try:
    # 1. Pedir saludo
    print(f"Conectando a {url}/hello ...")
    res_hello = urllib.request.urlopen(f"{url}/hello")
    data_hello = json.loads(res_hello.read())
    print(f"Respuesta recibida: {data_hello}")

    # 2. Pedir hora
    print(f"Conectando a {url}/time ...")
    res_time = urllib.request.urlopen(f"{url}/time")
    data_time = json.loads(res_time.read())
    print(f"Respuesta recibida: {data_time}")

except Exception as e:
    print(f"ERROR: No se pudo conectar. {e}")
